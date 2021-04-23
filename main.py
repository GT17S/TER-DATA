import multiprocessing
import threading

import pandas as pd  # (version 1.0.0)
import plotly  # (version 4.5.0)
import plotly.express as px
import Connection as cx
import matplotlib.pyplot as plt
import dash  # (version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# print(px.data.gapminder()[:15])


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
it = pd.read_sql_query('''select nicename from countries''', cx.conn)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in it.nicename],
            multi=True,
            value="nicename",
            id="input_state"
        ),
        html.Button(id='submit_button', n_clicks=0, children='Submit'),
        html.Div(id='output_state'),
    ], style={'text-align': 'center'}),

])


# ---------------------------------------------------------------
@app.callback(
    [Output('output_state', 'children'),
     Output(component_id='the_graph', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='input_state', component_property='value')]
)
def update_output(num_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df = pd.read_sql_query('''select nicename,year,value as value from bsa,countries where country=nicename ''',
                               cx.conn)
        fig = px.choropleth(df, locations='nicename', color='value',
                            locationmode='country names',
                            color_continuous_scale=px.colors.sequential.Plasma,
                            title='Regions with Positive Cases', animation_frame='year',
                            )

        fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center'),
                          margin=dict(l=60, r=60, t=50, b=50))
        if num_clicks >= 1:
            inche(val_selected)

        return ('Le pays est : "{}" '.format(val_selected), fig)


def inche(str):
    cursor = cx.conn.cursor()
    t = ("SELECT id FROM countries WHERE nicename= %s "
         )

    # Execute cursor.
    test1 = ('''
    select personal,year
    from gmi g,countries s
    where g.country_id=s.id and s.nicename=%s
    ''')
    df1 = pd.read_sql_query(test1, cx.conn, params=str)

    test2 = ('''select B.year , B.value
                from bsa B , countries C 
                 where C.id = B.country_id 
                and C.nicename=%s ''')

    df2 = pd.read_sql_query(test2, cx.conn, params=str)

    test3 = ('''select I.year , I.percentage_of_total_population
                    from imigration I  , countries C 
                     where C.id = I.country_id 
                     and C.nicename=%s ''')

    df3 = pd.read_sql_query(test3, cx.conn, params=str)

    test4 = ('''select IP.year , IP.value
                from ipu IP  , countries C 
                where C.id = IP.country_id 
                and C.nicename=%s ''')

    df4 = pd.read_sql_query(test4, cx.conn, params=str)

    test5 = ('''SELECT P.value::numeric(10,2) as value  , P.year as year
    FROM countries C , countries_in_regions CIR , world_regions WR , pib P  where  
    CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id and C.nicename=%s''')

    df5 = pd.read_sql_query(test5, cx.conn, params=str)

    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    root = tk.Tk()

    figure1 = plt.Figure(figsize=(3, 2), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.plot(df1['year'], df1['personal'], color='red')
    scatter1 = FigureCanvasTkAgg(figure1, root)
    scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax1.legend([''])
    ax1.set_xlabel('valeur de personals')
    ax1.set_title('ev de personal ')

    figure2 = plt.Figure(figsize=(3, 2), dpi=100)
    ax2 = figure2.add_subplot(111)
    ax2.plot(df2['year'], df2['value'], color='red')
    scatter2 = FigureCanvasTkAgg(figure2, root)
    scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax2.legend([''])
    ax2.set_xlabel('valeur BSA')
    ax2.set_title('Evolutiion des valeurs BSA depuis 1990 ')

    figure3 = plt.Figure(figsize=(3, 2), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.plot(df3['year'], df3['percentage_of_total_population'], color='red')
    scatter3 = FigureCanvasTkAgg(figure3, root)
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.legend([''])
    ax3.set_xlabel("taux d'imigration")
    ax3.set_title("Evolution des taux d'imigratan exprimé en %  ")

    figure4 = plt.Figure(figsize=(3, 2), dpi=100)
    ax4 = figure4.add_subplot(111)
    ax4.plot(df4['year'], df4['value'], color='green')
    scatter4 = FigureCanvasTkAgg(figure4, root)
    scatter4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax4.legend([''])
    ax4.set_xlabel(" % utilisation internet")
    ax4.set_title("Evolution utulisation internet  exprimé en %  ")

    figure5 = plt.Figure(figsize=(3, 2), dpi=100)
    ax5 = figure5.add_subplot(111)
    ax5.scatter(df5['year'], df5['value'], color='g')
    scatter5 = FigureCanvasTkAgg(figure5, root)
    scatter5.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax5.legend(['PIB'])
    ax5.set_xlabel('vlauer de pib')
    ax5.set_title('ev de pib depuis 1990')

    root.mainloop()


if __name__ == '__main__':
    plt.switch_backend('agg')
    app.run_server(debug=True, use_reloader=False)