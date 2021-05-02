import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file

# Connect to your app pages
from apps import bsa,compar
app.app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Comparaison', href='/apps/vgames')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/global_sales':
        return compar.layout
    elif pathname == '/apps/global_sales':
        return bsa.layout
    else:
        return bsa.layout


if __name__ == '__main__':
    app.app.run_server(debug=False)