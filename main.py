import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.apps import bsa,compar,app


app.app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link(' Cliquez ici pour la comparaison des différentes données ', href='/src/apps/compar',style={"color": "red", "size":"30"}),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/src/apps/compar':
        return compar.layout
    else:
        return bsa.layout


if __name__ == '__main__':
    app.app.run_server(debug=False)