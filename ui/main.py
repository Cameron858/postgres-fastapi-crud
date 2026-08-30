import requests
from dash import MATCH, Dash, Input, Output, State, ctx, dcc, html, no_update

app = Dash()
server = app.server


def create_task_element(id, content):
    return html.Li(
        html.Div(
            [
                f"{content}",
                dcc.Button("Delete", id={"type": "delete-task-btn", "index": id}),
            ]
        ),
        id=f"task_{id}",
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


app.layout = html.Div(
    [
        html.H1("Todo"),
        html.Div(
            [
                dcc.Input(
                    id="new-task-input",
                    type="text",
                    placeholder="",
                    debounce=True,
                    style={"flex": "1", "minWidth": 0},
                ),
                dcc.Button("Create", id="create-btn", n_clicks=0),
            ],
            style={
                "display": "flex",
                "gap": "10px",
                "alignItems": "center",
                "width": "100%",
            },
        ),
        html.Div(id="task-list", children=get_tasks()),
    ],
    style={
        "maxWidth": "700px",
        "margin": "0 auto",
        "padding": "20px",
        "boxSizing": "border-box",
        "width": "100%",
    },
)


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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
