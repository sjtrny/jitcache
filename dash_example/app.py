import dash
import dash_html_components as html
import time
from jitcache import KVStore
import json

store = KVStore()

app = dash.Dash(__name__)

server = app.server
app.layout = html.Div(
    children=[
        html.Button("Submit", id="button"),
        html.Div(id="output-container-button1", children=[]),
        html.Div(id="output-container-button2", children=[]),
    ]
)


# This is only called once per click
def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


@app.callback(
    dash.dependencies.Output("output-container-button1", "children"),
    [dash.dependencies.Input("button", "n_clicks")],
)
def update_output1(n_clicks):
    input_1 = n_clicks if n_clicks is not None else 0
    input_2 = 2

    kwarg_dict = {"input_1": input_1, "input_2": input_2}

    # Make a unique identifier for this object
    key = json.dumps(kwarg_dict, sort_keys=True)

    value = store.get_value(key, slow_fn, kwarg_dict)

    return f"Value is {value} and the button has been clicked {n_clicks} times"


@app.callback(
    dash.dependencies.Output("output-container-button2", "children"),
    [dash.dependencies.Input("button", "n_clicks")],
)
def update_output2(n_clicks):
    input_1 = n_clicks if n_clicks is not None else 0
    input_2 = 2

    kwarg_dict = {"input_1": input_1, "input_2": input_2}

    # Make a unique identifier for this object
    key = json.dumps(kwarg_dict, sort_keys=True)

    value = store.get_value(key, slow_fn, kwarg_dict)

    return f"Value is {value} and the button has been clicked {n_clicks} times"


if __name__ == "__main__":
    app.run_server(debug=True)
