import os
import sys
from typing import List, Dict, Any, Optional

import pymssql
from pymssql import Connection

# import sqlite3
# from sqlite3 import Connection
from dotenv import load_dotenv
import logging

from models.database import insert_parsed_data
from logiwa.api import get_api_token, get_shipments


def load_from_staging(conn: Connection) -> Optional[List[Dict[str, Any]]]:
    select_query = """
    SELECT order_id, raw_json, fetch_timestamp
    FROM staging_warehouse_orders
    ORDER BY fetch_timestamp DESC
    LIMIT ?
    """

    return []


def save_shipments_to_sql(conn: Connection):
    for shipment in shipments:
        if not insert_parsed_data(connection=conn, parsed_data=shipment):
            logging.error("failed to insert shipment")

    logging.info(f"Saved {len(shipments)} shipments to SQL.")

    return


def main() -> int:
    if get_api_token():
        logging.error("got API token from Logiwa")
    else:
        logging.error("failed to get API token")
        return -1

    conn = pymssql.connect(
        server=os.getenv("SQL_SERVER_NAME"),
        user=os.getenv("SQL_USER_NAME"),
        password=os.getenv("SQL_PASSWORD"),
        database=os.getenv("SQL_DATABASE_NAME"),
    )

    # conn = sqlite3.connect("shipments.db")

    get_shipments(conn)

    save_shipments_to_sql(conn)
    conn.close()

    return 0


if __name__ == "__main__":
    if not load_dotenv():
        logging.error("failed to load dotenv")
        sys.exit(1)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    sys.exit(main())
