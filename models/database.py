"""
Database insertion module using SQLAlchemy
"""

import sqlite3
from typing import Dict, Any, List
from sqlite3 import Error
from datetime import datetime
from dataclasses import asdict
from decimal import Decimal


def _dataclass_to_dict(obj) -> Dict[str, Any]:
    """Convert dataclass to dictionary, handling datetime and Decimal"""
    data = asdict(obj)
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, Decimal):
            data[key] = float(value)
    return data


def insert_order(connection: sqlite3.Connection, order) -> bool:
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
        # placeholders = ", ".join(["%s"] * len(order_dict)) # mssql
        placeholders = ", ".join(["?"] * len(order_dict)) # sqlite3
        query = f"INSERT OR IGNORE INTO shipment_order ({columns}) VALUES ({placeholders})"

        cursor.execute(query, list(order_dict.values()))
        connection.commit()
        print(f"Inserted order ID: {order.id}")
        return True
    except Error as e:
        print(f"Error inserting order: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_order_lines(connection: sqlite3.Connection, lines: List) -> bool:
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
            # placeholders = ", ".join(["%s"] * len(line_dict)) # mssql
            placeholders = ", ".join(["?"] * len(line_dict)) # sqlite3
            query = (
                f"INSERT OR IGNORE INTO shipment_order_line ({columns}) VALUES ({placeholders})"
            )

            cursor.execute(query, list(line_dict.values()))

        connection.commit()
        print(f"Inserted {len(lines)} order lines")
        return True
    except Error as e:
        print(f"Error inserting order lines: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_addresses(connection: sqlite3.Connection, addresses: List) -> bool:
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
            # placeholders = ", ".join(["%s"] * len(address_dict)) # mssql
            placeholders = ", ".join(["?"] * len(address_dict)) # sqlite3
            query = f"INSERT OR IGNORE INTO shipment_order_address ({columns}) VALUES ({placeholders})"

            cursor.execute(query, list(address_dict.values()))

        connection.commit()
        print(f"Inserted {len(addresses)} addresses")
        return True
    except Error as e:
        print(f"Error inserting addresses: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_mappings(
    connection: sqlite3.Connection, mappings: List, table_name: str
) -> bool:
    """Insert mapping records for junction tables"""
    if not mappings:
        return True

    cursor = None
    try:
        cursor = connection.cursor()

        for mapping in mappings:
            mapping_dict = _dataclass_to_dict(mapping)
            mapping_dict.pop("id")  # Auto-generated
            mapping_dict.pop("created_at", None)

            columns = ", ".join(mapping_dict.keys())
            # placeholders = ", ".join(["%s"] * len(mapping_dict)) # mssql
            placeholders = ", ".join(["?"] * len(mapping_dict)) # sqlite3
            query = (
                # f"INSERT OR IGNORE IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})" # mysql string
                f"INSERT OR IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})" # sqlite3 string
            )

            cursor.execute(query, list(mapping_dict.values()))

        connection.commit()
        print(f"Inserted {len(mappings)} records into {table_name}")
        return True
    except Error as e:
        print(f"Error inserting mappings into {table_name}: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_errors(connection: sqlite3.Connection, errors: List) -> bool:
    """Insert error records"""
    if not errors:
        return True

    cursor = None
    try:
        cursor = connection.cursor()

        for error in errors:
            error_dict = _dataclass_to_dict(error)
            error_dict.pop("id")  # Auto-generated
            error_dict.pop("created_at", None)

            columns = ", ".join(error_dict.keys())
            # placeholders = ", ".join(["%s"] * len(error_dict)) # mssql
            placeholders = ", ".join(["?"] * len(error_dict)) # sqlite3
            query = (
                f"INSERT OR IGNORE INTO shipment_order_error ({columns}) VALUES ({placeholders})"
            )

            cursor.execute(query, list(error_dict.values()))

        connection.commit()
        print(f"Inserted {len(errors)} errors")
        return True
    except Error as e:
        print(f"Error inserting errors: {e}")
        connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


def insert_parsed_data(
    connection: sqlite3.Connection, parsed_data: Dict[str, Any]
) -> bool:
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

        # 1. Insert main order
        success &= insert_order(connection, parsed_data["order"])

        # 2. Insert order lines
        success &= insert_order_lines(connection, parsed_data["lines"])

        # 3. Insert addresses
        success &= insert_addresses(connection, parsed_data["addresses"])

        # 4. Insert all mappings
        success &= insert_mappings(
            connection, parsed_data["status_mappings"], "shipment_order_status_mapping"
        )
        success &= insert_mappings(
            connection,
            parsed_data["carrier_mappings"],
            "shipment_order_carrier_mapping",
        )
        success &= insert_mappings(
            connection,
            parsed_data["channel_mappings"],
            "shipment_order_channel_mapping",
        )
        success &= insert_mappings(
            connection,
            parsed_data["custom_status_mappings"],
            "shipment_order_custom_status_mapping",
        )
        success &= insert_mappings(
            connection,
            parsed_data["fba_status_mappings"],
            "shipment_order_fba_status_mapping",
        )

        # 5. Insert errors
        success &= insert_errors(connection, parsed_data["errors"])

        return success

    except Exception as e:
        print(f"Error in insert_parsed_data: {e}")
        return False
