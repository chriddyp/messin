import pandas.io.data as web

from dash.react import Dash
from dash.components import (div, h2, label,
    PlotlyGraph, Dropdown)

from datetime import datetime as dt
df = web.DataReader(
    "aapl", 'yahoo',
    dt(2007, 10, 1), dt(2009, 4, 1))

dash = Dash(__name__)

dash.layout = div([
    h2('hello dash'),
    div([
        label('select y data'),
        Dropdown(id='ydata', options=[{'val': c, 'label': c}
                                      for c in df.columns])
    ]),
    PlotlyGraph(id='graph')
])


@dash.react('graph', ['ydata'])
def update_graph(ydata_dropdown):
    return {
        'figure': {
            'data': [{
                'x': df.index,
                'y': df[ydata_dropdown.selected],
                'mode': 'markers'
            }],
            'layout': {
                'yaxis': {'title': ydata_dropdown.selected},
                'margin': {'t': 0}
            }
        }
    }

if __name__ == '__main__':
    dash.server.run(port=8080, debug=True)
