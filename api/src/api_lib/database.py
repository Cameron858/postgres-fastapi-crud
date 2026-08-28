import psycopg2
from psycopg2.extensions import connection


def create_connection() -> connection:
    """Create a PostgreSQL database connection."""
    return psycopg2.connect(
        user="postgres",
        host="db",
        port="5432",
        password="mysecretpassword",
    )


def get_conn():
    """Yield a database connection and close it after use."""
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()
