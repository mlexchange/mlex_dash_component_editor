# MLExchange Dash component editor
This script creates adaptive Dash GUI components from keyword pairs (JSON format).

It currently supports 8 types of Dash GUI components: 3 types of [input forms](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/) (int, float, str), [slider](https://dash.plotly.com/dash-core-components/slider), [dropdown](https://dash.plotly.com/dash-core-components/dropdown), [radio items](https://dash.plotly.com/dash-core-components/radioitems), [boolean toggle switch](https://dash.plotly.com/dash-daq/toggleswitch), and [image](https://dash.plotly.com/dash-html-components/img). The corresponding keyword values are 'int', 'float', 'str', 'slider', 'dropdown', 'radio', 'bool', and 'img'.

Legal keyword pairs: {'type': xxx, 'name': xxx, 'title': xxx, 'param_key': xxx, 'value': xxx} and all the other legal keyword pairs in the corresponding Dash components. **Note**: 'name' is the unique string identifier.



## Dependencies:

```
dash>=2.9.0
dash_bootstrap_components>=1.0.0
dash_daq>=0.1.0
werkzeug==2.0
```


## Code example

```python
from dash import Dash, html
from dash_component_editor import JSONParameterEditor

# data
component_kwargs = {"gui_parameters": [{"type": "int", "name": "num-tree", "title": "Number of Trees", "param_key": "n_estimators", "value": "30"}, 
                                       {"type": "int", "name": "tree-depth", "title": "Tree Depth", "param_key": "max_depth", "value": "8"}]}


# set up Dash server and web layouts
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
```


