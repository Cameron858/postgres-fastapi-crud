import os

import psycopg2
from psycopg2.extensions import connection


def create_connection() -> connection:
    """Create a PostgreSQL database connection using environment variables."""
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.environ["POSTGRES_PASSWORD"],
    )


def get_conn():
    """Yield a database connection and close it after use."""
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()
