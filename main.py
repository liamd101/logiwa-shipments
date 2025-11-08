import os
import sys

import pymssql
from pymssql import Connection
# import sqlite3
# from sqlite3 import Connection

from dotenv import load_dotenv
import logging
import datetime

from models.database import insert_parsed_data
from models.parsing import WarehouseOrderParser
from logiwa.api import get_api_token, get_shipments


def process_shipments(conn: Connection) -> bool:
    """
    Transfers all data from the staging table to the final tables
    Returns true if it successfully emptied the staging table. False otherwise.
    """
    success = True
    cur = conn.cursor()
    select_query = "SELECT raw_json FROM dbo.ShipmentOrder_Staging" # pymssql
    # select_query = "SELECT raw_json FROM ShipmentOrder_Staging"  # sqlite3
    cur.execute(select_query)
    orders = cur.fetchall()
    for order_data in orders:
        shipment = WarehouseOrderParser().parse_response(order_data[0])
        success &= insert_parsed_data(conn, shipment)
        order_data = cur.fetchone()

    # return False if any orders failed for any reason
    return success


def main() -> int:
    start_time = datetime.datetime.now()
    success = False

    conn = pymssql.connect(
        server=os.getenv("SQL_SERVER_NAME"),
        user=os.getenv("SQL_USER_NAME"),
        password=os.getenv("SQL_PASSWORD"),
        database=os.getenv("SQL_DATABASE_NAME"),
    )

    # conn = sqlite3.connect("shipments.db")

    try:
        if get_api_token():
            logging.info("got API token from Logiwa")
        else:
            logging.error("failed to get API token")
            return -1

        shipments = get_shipments(conn)
        if not shipments:
            logging.error("failed to get shipments from API")
            return -1

        if process_shipments(conn):
            conn.cursor().execute("TRUNCATE table dbo.ShipmentOrder_Staging") # pymssql
            # conn.cursor().execute("DELETE FROM ShipmentOrder_Staging")  # sqlite3
            conn.commit()

        success = True
        return 0
    except Exception as e:
        logging.error(f"main: {e}")
        return -1
    finally:
        conn.cursor().execute(
            "INSERT INTO dbo.ShipmentOrder_Runs (fetch_timestamp, success) VALUES (%s, %s)",
            (start_time, success),
        )  # pymssql
        # conn.cursor().execute(
        #     "INSERT INTO ShipmentOrder_Runs (fetch_timestamp, success) VALUES (?, ?)",
        #     (start_time.isoformat(), success),
        # )  # sqlite3
        conn.commit()
        conn.close()


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
