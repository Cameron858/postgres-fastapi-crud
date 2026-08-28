from typing import Annotated

import psycopg2.extras
from api_lib.database import get_conn
from fastapi import Depends, FastAPI
from psycopg2.extensions import connection

app = FastAPI()


@app.get("/health")
def status():
    """Return the API health status."""
    return {"status": "ok"}


@app.get("/items")
def items(conn: Annotated[connection, Depends(get_conn)]):
    """Return all items from the database."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM list")

        items = [dict(row) for row in cur.fetchall()]

    return items
