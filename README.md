[![Build Status](https://travis-ci.org/sjtrny/jitcache.svg?branch=master)](https://travis-ci.org/sjtrny/jitcache)
[![Documentation Status](https://readthedocs.org/projects/jitcache/badge/?version=latest)](https://jitcache.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/jitcache)](https://pepy.tech/project/jitcache)

# jitcache

Python function caching that prevents re-entrant calls

Standard caches such as Python's `func_tools.lru_cache` will allow repeated execution of a long-running function until the first successful completion. In contrast jitcache will block multiple calls until the first is completed, thus avoiding repeated computation.

jitcache was designed to improve the performance of Plot.ly Dash apps by caching results and reducing CPU load.

Installation
-------------------

Install via pip:

    $ pip install jitcache

Documentation
-------------------

Full documentation available here [https://jitcache.readthedocs.io/](https://jitcache.readthedocs.io/en/latest/)

Basic Usage
-------------------

    from jitcache import Cache
    import time
    
    
    cache = Cache()
    
    
    @cache.memoize
    def slow_fn(input_1, input_2, input_3=10):
        print("Slow Function Called")
        time.sleep(1)
        return input_1 * input_2 * input_3
    
    
    print(slow_fn(10, 2))


 Output:
 
    Slow Function Called
    40


Plot.ly Dash Usage
-------------------

    import dash
    import dash_html_components as html
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
    def update_output2(input_dropdown):
        print("run2")
    
        return input_dropdown
    
    
    if __name__ == "__main__":
        app.run_server(debug=True)
