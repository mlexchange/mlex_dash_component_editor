from dash import Dash, html
from dash_component_editor import JSONParameterEditor
import json

# data
component_kwargs = {"gui_parameters": [{"type": "int", "name": "num-tree", "title": "Number of Trees", "param_key": "n_estimators", "value": "30"}, 
                                       {"type": "int", "name": "tree-depth", "title": "Tree Depth", "param_key": "max_depth", "value": "8"}]}


# Set up Dash server and web layouts
app = Dash(__name__)
app.layout = html.Div ([html.Button('Show GUI', id='button', n_clicks=0),
                        html.Div(id='gui-layout', children=[])
                       ])


# callback 
@app.callback(
    Output("gui-layout", "children", allow_duplicate=True),
    Input("button", "n_clicks"),
    prevent_initial_call=True
)
def show_gui_layouts(n_clicks):
    item_list = JSONParameterEditor(_id={'type': 'parameter_editor'},
                                    json_blob=component_kwargs["gui_parameters"],
                                )
    item_list.init_callbacks(app)
    
    return [html.H5("GUI Layout", className="card-title"), item_list]

