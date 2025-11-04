import os
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import json
from logging import debug, error
import requests
import time

from pymssql import Connection
# from sqlite3 import Connection

from models.database import last_fetched_date


API_TOKEN: Optional[str] = None

# Global rate limit configuration
MAX_REQUESTS_PER_MINUTE = 60  # Adjust this as needed


def get_api_token() -> bool:
    """
    Retrieves an API token for the Logiwa WMS API
    """
    global API_TOKEN

    url = "https://hubapi.logiwa.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    body = f"grant_type=password&username={os.getenv('LOGIWA_USERNAME')}&password={os.getenv('LOGIWA_PASSWORD')}"
    res = requests.post(url, data=body, headers=headers)

    res_body = res.json()
    if res_body.get("access_token"):
        API_TOKEN = str(res_body["access_token"])
        return True
    else:
        error(res_body.get(".error"))
        return False


def get_warehouses() -> Optional[List[int]]:
    url = "https://hubapi.logiwa.com/en/api/IntegrationApi/LookUp"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "LookupList": [2],  # get warehouse IDs only
    }
    res = requests.post(url, json=params, headers=headers)
    response_data = res.json()
    if res.status_code != 200:
        error(response_data)
        return None
    else:
        warehouses = [
            warehouse["Id"]
            for warehouse in response_data["Lookup"].get("WarehouseList")
        ]
        return warehouses


def fetch_page(
    warehouse: int,
    page_index: int,
    window: timedelta,
    headers: Dict[str, str],
    url: str,
    last_modified_date: Optional[datetime],
) -> Optional[List[Dict[str, Any]]]:
    """Fetch a single page of data"""
    params = {
        "OrderDate_Start": (datetime.now() - window).strftime("%m.%d.%Y %H:%M:%S"),
        "OrderDate_End": (datetime.now() + window).strftime("%m.%d.%Y %H:%M:%S"),
        "IsGetOrderDetails": True,
        "IsGetCustomerAddressInfo": True,
        "WarehouseID": warehouse,
        "PageSize": 200,
        "SelectedPageIndex": page_index,
    }
    if last_modified_date:
        params["LastModifiedDate_Start"] = last_modified_date.strftime(
            "%m.%d.%Y %H:%M:%S"
        )

    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 403:
        time.sleep(2)
        # recursively call it incase it continues to fail
        return fetch_page(
            warehouse,
            page_index,
            window,
            headers,
            url,
            last_modified_date,
        )

    response_data = response.json()
    data = response_data.get("Data", [])
    debug(f"Warehouse {warehouse}, Page {page_index}: Received {len(data)} orders")

    return data if data else None


def fetch_warehouse_pages(
    conn: Connection,
    warehouse: int,
    window: timedelta,
    headers: Dict[str, str],
    url: str,
    last_modified_date: Optional[datetime],
):
    """Fetch all pages for a single warehouse"""
    debug(f"Processing shipments out of warehouse {warehouse}")
    page_index = 1

    # delete_query = (
    #     "DELETE FROM dbo.ShipmentOrder_Staging WHERE order_id = %s"  # pymssql
    # )
    # insert_query = """
    # INSERT INTO dbo.ShipmentOrder_Staging (order_id, raw_json, fetch_timestamp)
    # SELECT (%s, %s, %s)
    # """  # pymssql

    delete_query = "DELETE FROM ShipmentOrder_Staging WHERE order_id = ?"  # sqlite3
    insert_query = """
    INSERT INTO ShipmentOrder_Staging (order_id, raw_json, fetch_timestamp)
    VALUES (?, ?, ?)
    """  # sqlite3

    cur = conn.cursor()
    while True:
        if page_index > 1:
            break
        orders = fetch_page(
            warehouse,
            page_index,
            window,
            headers,
            url,
            last_modified_date,
        )
        if orders is None:
            break

        for order in orders:
            order_id = order.get("ID")
            raw_json = json.dumps(order)
            fetch_timestamp = datetime.now()

            cur.execute(delete_query, (order_id,))
            cur.execute(
                insert_query,
                (
                    order_id,
                    raw_json,
                    fetch_timestamp,
                ),
            )

        page_index += 1

    conn.commit()


# create new table with
# order_date   = 10/21
# modified_date = 10/22
# dbo.ShipmentOrder_Retrievals (datetime)
# store the datetime of the most recent successful run

def get_shipments(conn: Connection) -> bool:
    """
    Queries the Logiwa API synchronously and returns a boolean indicating Success (True) or failure (False)
    Shipments are only queried within the past or next 45 days

    Shipments are stored in a staging table for future access
    """
    warehouses = get_warehouses()
    if not warehouses:
        return False

    url = "https://hubapi.logiwa.com/en/api/IntegrationApi/WarehouseOrderSearch"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    window = timedelta(days=45)
    last_modified_date_stored = last_fetched_date(conn)

    # Fetch all warehouses sequentially
    for warehouse in warehouses:
        fetch_warehouse_pages(
            conn,
            warehouse,
            window,
            headers,
            url,
            last_modified_date_stored,
        )

    return True
