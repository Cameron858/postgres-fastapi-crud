import requests
from dash import MATCH, Dash, Input, Output, State, ctx, no_update

from ui_lib import get_tasks


def register_callbacks(app: Dash):
    @app.callback(
        Output("task-list", "children", allow_duplicate=True),
        Output("new-task-input", "value"),
        Input("create-btn", "n_clicks"),
        State("new-task-input", "value"),
        prevent_initial_call=True,
    )
    def create_task(n_clicks, value):
        if n_clicks is None or n_clicks < 1:
            return no_update, no_update

        if value and value.strip():
            requests.post("http://api:8080/items/", json={"content": value.strip()})

        return get_tasks(), ""

    @app.callback(
        Output("task-list", "children", allow_duplicate=True),
        Input({"type": "delete-task-btn", "index": MATCH}, "n_clicks"),
        prevent_initial_call=True,
    )
    def delete_task(n_clicks):
        if n_clicks is None or n_clicks < 1:
            return no_update

        requests.delete(f"http://api:8080/items/{ctx.triggered_id['index']}")  # type: ignore
        return get_tasks()
