import os
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import json
from logging import debug, info, error
import requests
import time

from pymssql import Connection
# from sqlite3 import Connection

from models.parsing import WarehouseOrderParser


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
    last_modified_date: Optional[str],
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
        params["LastModifiedDate_Start"] = datetime.strptime(
            last_modified_date, "%Y-%m-%d %H:%M:%S"
        ).strftime("%m.%d.%Y %H:%M:%S")

    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 403:
        time.sleep(2)
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
    last_modified_date: Optional[str],
):
    """Fetch all pages for a single warehouse"""
    debug(f"Processing shipments out of warehouse {warehouse}")
    all_orders = []
    page_index = 1

    # insert_query = """
    # INSERT INTO staging_shipment_order (order_id, raw_json, fetch_timestamp)
    # VALUES (?, ?, ?)
    # """  # sqlite3
    insert_query = """
    INSERT INTO dbo.ShipmentOrder_Staging (order_id, raw_json, fetch_timestamp)
    VALUES (%s, %s, %s)
    """  # pymssql

    cur = conn.cursor()
    while True:
        data = fetch_page(
            warehouse,
            page_index,
            window,
            headers,
            url,
            last_modified_date,
        )
        if data is None:
            break

        for order_data in data:
            order_id = order_data.get("ID")
            raw_json = json.dumps(order_data)
            fetch_timestamp = datetime.now()

            cur.execute(insert_query, (order_id, raw_json, fetch_timestamp))

        all_orders.extend(data)
        page_index += 1

    conn.commit()
    conn.close()


def get_most_recent_modified_date(conn: Connection) -> Optional[str]:
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(last_modified_date) FROM shipment_order")
    result = cursor.fetchone()
    return result[0] if result and result[0] is not None else None


def get_shipments(conn: Connection):
    """
    Queries the Logiwa API synchronously and returns a List of ShipmentInfo
    Shipments are only queried within the past or next 45 days
    """
    warehouses = get_warehouses()
    if not warehouses:
        return None

    url = "https://hubapi.logiwa.com/en/api/IntegrationApi/WarehouseOrderSearch"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    window = timedelta(days=45)
    last_modified_date_stored = get_most_recent_modified_date(conn)

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
