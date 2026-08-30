import requests
from dash import dcc, html


def create_task_element(task_id, content):
    return html.Li(
        html.Div(
            [
                f"{content}",
                dcc.Button(
                    "Delete",
                    id={"type": "delete-task-btn", "index": task_id},
                    style={"margin-left": "1rem"},
                ),
            ]
        ),
        id=f"task_{task_id}",
    )


def get_tasks():
    return html.Ul(
        [
            create_task_element(task["id"], task["content"])
            for task in sorted(
                requests.get("http://api:8080/items/").json(), key=lambda x: x["id"]
            )
        ]
    )


__all__ = ["create_task_element", "get_tasks"]
