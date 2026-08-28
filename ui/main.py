from dash import Dash, html

app = Dash()

app.layout = [
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
