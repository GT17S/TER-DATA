import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input ,Output
import plotly.express as px
import pandas as pd
import Database.conxion as cx
import app


test5 = pd.read_sql_query('''SELECT C.name as name  , P.value::numeric(10,2) as value  , P.year as year ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , pib P  where  
CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id order by C.name''',cx.conn)

all_continents = test5.continent.unique()
layout = html.Div([
    dcc.Checklist(
        id= "checklist",
        options=[{"label" : x ,"value" : x }
                  for x in all_continents],
        value=all_continents[4:],
        labelStyle={'display':'inline-block'}
    ),
    dcc.Graph(id= "line-chart"),
])

@app.app.callback(
    Output("line-chart","figure"),
    [Input("checklist","value")])

def update_line_chart(con):
    mask = test5.continent.isin(con)
    fig = px.line(test5[mask],
         x = "year", y = "value", color = 'name',title = "Le PIB des pays classé par continent entre 1990 et 2019 ")
    return  fig

