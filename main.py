import sys
from typing import Optional, List, Dict, Any
import sqlite3
from dotenv import load_dotenv

from models.database import insert_parsed_data
from logiwa.api import get_api_token, get_shipments


def save_shipments_to_sql(shipments: List[Dict[str, Any]]):
    conn = sqlite3.connect("shipments.db")

    for shipment in shipments:
        if not insert_parsed_data(connection=conn, parsed_data=shipment):
            print("failed to insert shipment")

    return


def main() -> int:
    if get_api_token():
        print("got API token from Logiwa")
    else:
        print("failed to get API token")
        return -1

    shipments = get_shipments()
    if shipments is None:
        print("failed to contact Logiwa API")
        return -1

    save_shipments_to_sql(shipments)

    return 0


if __name__ == "__main__":
    if not load_dotenv():
        print("failed to load dotenv")
        sys.exit(1)
    sys.exit(main())
