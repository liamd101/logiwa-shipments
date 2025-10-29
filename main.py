import os
import sys
from typing import List, Dict, Any
import pymssql
from pymssql import Connection
from dotenv import load_dotenv
import logging

from models.database import insert_parsed_data
from logiwa.api import get_api_token, get_shipments


def save_shipments_to_sql(conn: Connection, shipments: List[Dict[str, Any]]):
    for shipment in shipments:
        if not insert_parsed_data(connection=conn, parsed_data=shipment):
            print("failed to insert shipment")

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

    shipments = get_shipments(conn)
    if shipments is None:
        logging.error("failed to contact Logiwa API")
        return -1

    save_shipments_to_sql(conn, shipments)
    conn.close()

    return 0


if __name__ == "__main__":
    if not load_dotenv():
        print("failed to load dotenv")
        sys.exit(1)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    sys.exit(main())
