import os
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import json

import requests

from models.parsing import WarehouseOrderParser


API_TOKEN: Optional[str] = None

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
        print(res_body.get(".error"))
        return False


def get_shipments() -> Optional[List[Dict[str, Any]]]:
    """
    Queries the Logiwa API and returns a List of ShipmentInfo
    Shipments are only queried within the past or next 45 days
    """
    url = "https://hubapi.logiwa.com/en/api/IntegrationApi/WarehouseOrderSearch"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    window: timedelta = timedelta(days=45)

    params = {
        "OrderDate_Start": (datetime.now() - window).strftime("%m.%d.%Y %H:%M:%S"),
        "OrderDate_End": (datetime.now() + window).strftime("%m.%d.%Y %H:%M:%S"),
        "WarehouseID": 202,
        "PageSize": 10,
        "IsGetOrderDetails": True,
        "IsGetCustomerAddressInfo": True,
    }

    res = requests.post(url, json=params, headers=headers)
    response_data = res.json()

    with open("res.json", "w") as f:
        f.write(json.dumps(response_data, indent=2))

    shipments = []

    staging_file = open("data.jsonl", "a")

    for order_data in response_data.get("Data", []):
        staging_file.write(json.dumps(order_data) + "\n")
        shipment = WarehouseOrderParser().parse_response(order_data)
        if shipment:
            shipments.append(shipment)

    staging_file.close()

    return shipments

