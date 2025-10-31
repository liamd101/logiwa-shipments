"""
Database insertion module using SQLAlchemy
"""

from sqlite3 import Error, Connection

# from pymssql import Error, Connection
from typing import Dict, Any, List
from datetime import datetime
from dataclasses import asdict
from decimal import Decimal
import logging


def _dataclass_to_dict(obj) -> Dict[str, Any]:
    """Convert dataclass to dictionary, handling datetime and Decimal"""
    data = asdict(obj)
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, Decimal):
            data[key] = float(value)
    return data


def insert_order(connection: Connection, order) -> bool:
    """Insert main order record"""
    cursor = None
    try:
        cursor = connection.cursor()
        order_dict = _dataclass_to_dict(order)

        # Remove auto-generated timestamp fields if they're None
        order_dict.pop("api_fetch_timestamp", None)
        order_dict.pop("created_at", None)
        order_dict.pop("updated_at", None)

        columns = ", ".join(order_dict.keys())
        # placeholders = ", ".join(["%s"] * len(order_dict))  # pymssql
        # query = f"INSERT IGNORE INTO dbo.ShipmentOrder ({columns}) VALUES ({placeholders})"  # pymssql
        
        # cursor.execute("DELETE FROM dbo.ShipmentOrder WHERE id = %s", order.id)
        cursor.execute("DELETE FROM shipment_order WHERE id = ?", order.id)

        placeholders = ", ".join(["?"] * len(order_dict))  # sqlite3
        query = f"INSERT OR IGNORE INTO shipment_order ({columns}) VALUES ({placeholders})"  # sqlite3

        cursor.execute(query, list(order_dict.values()))
        connection.commit()
        logging.debug(f"Inserted order ID: {order.id}")
        return True
    except Error as e:
        logging.error(f"Error inserting order: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_order_lines(connection: Connection, lines: List) -> bool:
    """Insert order line items in batch"""
    if not lines:
        return True

    cursor = None
    try:
        cursor = connection.cursor()

        for line in lines:
            line_dict = _dataclass_to_dict(line)
            line_dict.pop("created_at", None)
            line_dict.pop("updated_at", None)

            columns = ", ".join(line_dict.keys())
            # placeholders = ", ".join(["%s"] * len(line_dict))  # pymssql
            # query = f"INSERT IGNORE INTO dbo.ShipmentOrder_Line ({columns}) VALUES ({placeholders})"  # pymssql
            placeholders = ", ".join(["?"] * len(line_dict))  # sqlite3
            query = f"INSERT OR IGNORE INTO shipment_order_line ({columns}) VALUES ({placeholders})"  # sqlite3

            cursor.execute(query, list(line_dict.values()))

        connection.commit()
        logging.debug(f"Inserted {len(lines)} order lines")
        return True
    except Error as e:
        logging.error(f"Error inserting order lines: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_addresses(connection: Connection, addresses: List) -> bool:
    """Insert address records"""
    if not addresses:
        return True

    cursor = None
    try:
        cursor = connection.cursor()

        for address in addresses:
            address_dict = _dataclass_to_dict(address)
            address_dict.pop("id")  # Auto-generated
            address_dict.pop("created_at", None)
            address_dict.pop("updated_at", None)

            columns = ", ".join(address_dict.keys())
            # placeholders = ", ".join(["%s"] * len(address_dict))  # pymssql
            # query = f"INSERT IGNORE INTO dbo.ShipmentOrder_Address ({columns}) VALUES ({placeholders})"  # pymssql
            placeholders = ", ".join(["?"] * len(address_dict))  # sqlite3
            query = f"INSERT OR IGNORE INTO shipment_order_address ({columns}) VALUES ({placeholders})"  # sqlite3

            cursor.execute(query, list(address_dict.values()))

        connection.commit()
        logging.debug(f"Inserted {len(addresses)} addresses")
        return True
    except Error as e:
        logging.error(f"Error inserting addresses: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def clean_staging_table(connection: Connection, id: int) -> bool:
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM staging_shipment_order WHERE order_id = ?", (id,))
        connection.commit()
        return True
    except Error as e:
        logging.error(f"Error deleting entry: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_parsed_data(connection: Connection, parsed_data: Dict[str, Any]) -> bool:
    """
    Insert all parsed data in correct order

    Args:
        parsed_data: Dictionary returned from WarehouseOrderParser.parse_response()

    Returns:
        bool: True if all inserts successful, False otherwise
    """
    try:
        # Insert in order of dependencies
        success = True

        success &= insert_order(connection, parsed_data["order"])
        success &= insert_order_lines(connection, parsed_data["lines"])
        success &= insert_addresses(connection, parsed_data["addresses"])

        if success:
            clean_staging_table(connection, parsed_data["order"].id)

        return success

    except Exception as e:
        logging.error(f"Error in insert_parsed_data: {e}")
        return False
