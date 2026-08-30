import requests
from dash import MATCH, Dash, Input, Output, State, ctx, dcc, html

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


app.layout = [
    html.H1("Todo"),
    html.Div(
        [
            dcc.Input(id="new-task-input", type="text", placeholder="", debounce=True),
            dcc.Button("Create", id="create-btn", n_clicks=0),
        ],
        style={"display": "flex"},
    ),
    get_tasks(),
    html.Div(id="container-button-basic", children="Enter a value and press submit"),
]


@app.callback(
    Output("container-button-basic", "children"),
    Input("create-btn", "n_clicks"),
    State("new-task-input", "value"),
    prevent_initial_call=True,
)
def update_output(n_clicks, value):
    requests.post("http://api:8080/items/", json={"content": value})


@app.callback(
    Input({"type": "delete-task-btn", "index": MATCH}, "n_clicks"),
    prevent_initial_call=True,
)
def delete_task(_):
    requests.delete(f"http://api:8080/items/{ctx.triggered_id['index']}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
