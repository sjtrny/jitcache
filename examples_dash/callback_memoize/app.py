import dash
import dash_html_components as html
import time
from jitcache import Cache
import dash_core_components as dcc


cache = Cache()

app = dash.Dash(__name__)

server = app.server
app.layout = html.Div(
    children=[
        html.Div(id="output-container-dropdown1", children=[]),
        html.Div(id="output-container-dropdown2", children=[]),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
            id="dropdown",
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("output-container-dropdown1", "children"),
    [dash.dependencies.Input("dropdown", "value")],
)
@cache.memoize
def update_output1(input_dropdown):
    print("run1")

    return input_dropdown


@app.callback(
    dash.dependencies.Output("output-container-dropdown2", "children"),
    [dash.dependencies.Input("dropdown", "value")],
)
@cache.memoize
def update_output1(input_dropdown):
    print("run2")

    return input_dropdown


if __name__ == "__main__":
    app.run_server(debug=True)
