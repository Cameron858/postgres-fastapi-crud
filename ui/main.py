import requests
from dash import Dash, html

app = Dash()
server = app.server


def create_task_element(id, content):
    return html.Li(html.Div(f"{content}"), id=f"task_{id}")


def get_tasks():
    return html.Ol(
        [
            create_task_element(task["id"], task["content"])
            for task in sorted(
                requests.get("http://api:8080/items/").json(), key=lambda x: x["id"]
            )
        ]
    )


app.layout = [html.H1("Todo"), get_tasks()]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
