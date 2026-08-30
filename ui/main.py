from dash import Dash, html

app = Dash()
server = app.server

mock_tasks = [
    {"id": 1, "content": "Buy more milk."},
    {"id": 2, "content": "Walk the dog."},
    {"id": 3, "content": "Find the cat."},
]


def get_tasks():
    return [html.Div(f"{t['id']} - {t['content']}") for t in mock_tasks]


app.layout = [html.H1("Todo"), *get_tasks()]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
