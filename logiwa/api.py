import os
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import json
from logging import debug, info, error
import asyncio
import aiohttp
import time
import requests

# from pymssql import Connection
from sqlite3 import Connection

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


# Global rate limit configuration (in milliseconds)
MIN_MS_BETWEEN_REQUESTS = 113  # Adjust this as needed (e.g., 100ms = 10 requests/sec)


class RateLimiter:
    """Simple rate limiter based on minimum time between requests"""

    def __init__(self, min_ms_between_requests: int):
        self.min_delay = min_ms_between_requests / 1000.0  # Convert to seconds
        self.last_request_time = 0
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.time()
            time_since_last = now - self.last_request_time

            if time_since_last < self.min_delay:
                # Wait for the remaining time
                sleep_time = self.min_delay - time_since_last
                await asyncio.sleep(sleep_time)

            self.last_request_time = time.time()


async def fetch_page(
    session: aiohttp.ClientSession,
    rate_limiter: RateLimiter,
    warehouse: int,
    page_index: int,
    window: timedelta,
    headers: Dict[str, str],
    url: str,
) -> Optional[List[Dict[str, Any]]]:
    """Fetch a single page of data"""
    await rate_limiter.acquire()

    params = {
        "OrderDate_Start": (datetime.now() - window).strftime("%m.%d.%Y %H:%M:%S"),
        "OrderDate_End": (datetime.now() + window).strftime("%m.%d.%Y %H:%M:%S"),
        "IsGetOrderDetails": True,
        "IsGetCustomerAddressInfo": True,
        "WarehouseID": warehouse,
        "PageSize": 200,
        "SelectedPageIndex": page_index,
    }

    try:
        async with session.post(url, json=params, headers=headers) as response:
            response_data = await response.json()
            data = response_data.get("Data", [])
            debug(
                f"Warehouse {warehouse}, Page {page_index}: Received {len(data)} orders"
            )
            return data if data else None
    except Exception as e:
        debug(f"Error fetching warehouse {warehouse}, page {page_index}: {e}")
        return None


async def fetch_warehouse_pages(
    session: aiohttp.ClientSession,
    rate_limiter: RateLimiter,
    warehouse: int,
    window: timedelta,
    headers: Dict[str, str],
    url: str,
) -> List[Dict[str, Any]]:
    """Fetch all pages for a single warehouse"""
    debug(f"Processing shipments out of warehouse {warehouse}")
    all_orders = []
    page_index = 1

    while True:
        data = await fetch_page(
            session, rate_limiter, warehouse, page_index, window, headers, url
        )
        if data is None:
            break

        all_orders.extend(data)
        page_index += 1

    return all_orders


async def get_shipments_async(conn: Connection) -> Optional[List[Dict[str, Any]]]:
    """
    Queries the Logiwa API asynchronously and returns a List of ShipmentInfo
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
    rate_limiter = RateLimiter(MIN_MS_BETWEEN_REQUESTS)

    async with aiohttp.ClientSession() as session:
        # Fetch all warehouses concurrently
        tasks = [
            fetch_warehouse_pages(
                session, rate_limiter, warehouse, window, headers, url
            )
            for warehouse in warehouses
        ]
        warehouse_results = await asyncio.gather(*tasks)

    # Flatten results and process
    all_orders = [
        order for warehouse_orders in warehouse_results for order in warehouse_orders
    ]

    insert_query = """
    INSERT INTO staging_warehouse_orders (order_id, raw_json, fetch_timestamp)
    VALUES (?, ?, ?)
    """  # sqlite3
    # insert_query = """
    # INSERT INTO staging_warehouse_orders (order_id, raw_json, fetch_timestamp)
    # VALUES (%s, %s, %s)
    # """ # pymssql

    cur = conn.cursor()
    # Write to staging file and parse
    shipments = []
    for order_data in all_orders:
        order_id = order_data.get("ID")
        raw_json = json.dumps(order_data)
        fetch_timestamp = datetime.now()

        cur.execute(insert_query, (order_id, raw_json, fetch_timestamp))
        shipment = WarehouseOrderParser().parse_response(order_data)
        if shipment:
            shipments.append(shipment)

    info(f"Pulled {len(shipments)} shipments from Logiwa")
    return shipments


def get_shipments(conn: Connection) -> Optional[List[Dict[str, Any]]]:
    """Synchronous wrapper for the async function"""
    return asyncio.run(get_shipments_async(conn))
