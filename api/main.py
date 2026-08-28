from typing import Annotated

import psycopg2.extras
from api_lib.database import get_conn
from api_lib.types import BaseItem, ItemResponse
from fastapi import Depends, FastAPI
from psycopg2.extensions import connection

app = FastAPI()


@app.get("/health")
def status():
    """Return the API health status."""
    return {"status": "ok"}


@app.get("/items/", response_model=list[ItemResponse])
def get_items(conn: Annotated[connection, Depends(get_conn)]):
    """Return all items from the database."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM list")

        items = [dict(row) for row in cur.fetchall()]

    return items


@app.post("/items/", response_model=ItemResponse)
def create_item(
    item: BaseItem,
    conn: Annotated[connection, Depends(get_conn)],
):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "INSERT INTO list (content) VALUES (%s) RETURNING id, content",
            (item.content,),
        )

        created_item = dict(cur.fetchone())  # type: ignore
        conn.commit()

    return created_item
