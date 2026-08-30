from dash import Dash, dcc, html
from ui_lib import get_tasks
from ui_lib.callbacks import register_callbacks

app = Dash()
server = app.server


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

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
