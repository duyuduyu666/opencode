from fastmcp import FastMCP
import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any, Optional
import os

mcp = FastMCP("MySQL Database Server")

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "test_db",
}


def get_connection() -> Optional[mysql.connector.MySQLConnection]:
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        return None


@mcp.tool()
def list_databases() -> str:
    conn = get_connection()
    if not conn:
        return "Failed to connect to MySQL server"
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        return "Available databases: " + ", ".join(databases)
    finally:
        conn.close()


@mcp.tool()
def list_tables(database: str = None) -> str:
    config = DB_CONFIG.copy()
    if database:
        config["database"] = database
    conn = mysql.connector.connect(**config)
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        if not tables:
            return f"No tables found in database '{config['database']}'"
        return "Tables: " + ", ".join(tables)
    finally:
        conn.close()


@mcp.tool()
def execute_query(query: str) -> str:
    conn = get_connection()
    if not conn:
        return "Failed to connect to database"
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            if not results:
                return "Query returned no results"
            return str(results)
        else:
            conn.commit()
            return f"Affected rows: {cursor.rowcount}"
    except Error as e:
        return f"Error: {str(e)}"
    finally:
        conn.close()


@mcp.tool()
def describe_table(table_name: str) -> str:
    conn = get_connection()
    if not conn:
        return "Failed to connect to database"
    try:
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        result = [f"{col[0]} ({col[1]})" for col in columns]
        return "Table structure:\n" + "\n".join(result)
    except Error as e:
        return f"Error: {str(e)}"
    finally:
        conn.close()


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
