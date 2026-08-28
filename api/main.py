import psycopg2.extras
from api_lib.database import get_conn
from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/health")
def status():
    """Return the API health status."""
    return {"status": "ok"}


@app.get("/items")
def items(conn=Depends(get_conn)):
    """Return all items from the database."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM list")

        items = cur.fetchall()

    return items
