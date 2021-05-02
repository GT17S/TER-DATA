from tkinter import Label, font

import xlwt
from xlwt import Workbook
import mplcursors
import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.0)
from tkinter import *
import plotly.express as px
import xlwings as xw
import self
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import hist
from yaml import scan

import Database.conxion as cx
import matplotlib.pyplot as plt
import dash             #(version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import app
import js2py

it=pd.read_sql_query('''select nicename from countries''',cx.conn)

layout = html.Div([
    html.Div([
        dcc.Link('Navigate to "/"', href='/'),
        html.Br(),

    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        dcc.Dropdown(
            options=[{'label':i,'value':i} for i in it.nicename],
            multi=True,
            value="nicename",
            id="input_state"
        ),
        html.Button(id='submit_button', n_clicks=0, children='Submit'),
        html.Div(id='output_state'),
    ],style={'text-align': 'center'}),

])

#---------------------------------------------------------------
@app.app.callback(
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

        fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                          margin=dict(l=60, r=60, t=50, b=50))
        if num_clicks>=1:
            inche(val_selected)

        return ('Le pays est : "{}" '.format(val_selected), fig)
def hide_widget(str):
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    test=('''select nicename,year,value as value from bsa,countries where country=%s ''')
    df = pd.read_sql_query(test, cx.conn, params=str)

    sheet1.write(0, 0, 'PAYS')
    sheet1.write(0, 1, 'Annee')
    sheet1.write(0, 2, 'Valeur')
    i=0
    for py,an,va in df.iterrows():
        i = i + 1
        sheet1.write(i, 0, py)
        sheet1.write(i, 1, an)
        sheet1.write(i, 2, va)

    wb.save('xlwt example.xls')

    print(str)
    print("it works")

def inche(str):
    import pandas as pd
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk
    import matplotlib.pyplot as plt
    from tkinter import ttk

    import matplotlib
    matplotlib.use("TkAgg")
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


    # from matplotlib.figure import Figure

    root = tk.Tk()

    root.geometry("1230x700")
    root.resizable(width=0, height=0)
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Courbes pour :'+format(', '.join(str)))
    tabControl.add(tab2, text='Courbes de comparison ')
    tabControl.pack(expand=1, fill="both")

    '''
    button_hide = Button(root, text="Masque les courbes pour la pays ", command=lambda: hide_widget(fram))
    button_hide.pack(pady=0)
    button_show = Button(root, text="afficher les courbes pour le pays ", command=lambda: show_widget(canva,fram))
    button_show.pack()
    '''
    fram = tk.Frame(tab1)
    fram.pack(fill='both', expand=True, padx=0, pady=0)
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    b1 = tk.Button(fram, text='Courbes pour :'+format(', '.join(str)), borderwidth=0,command=lambda :hide_widget(str))
    b1['font'] = myFont

    b1.pack()

    canva = tk.Canvas(fram)
    canva.pack(fill='both', expand=True)
    fram2 = tk.Frame(canva)
    fram2.pack(fill='both', expand=True)
    figure = plt.Figure(figsize=(12,12),dpi=100)
    scroll = Scrollbar(fram2, orient=VERTICAL, command=canva.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=True, anchor="ne")

    scroll2 = Scrollbar(fram2, orient=HORIZONTAL, command=canva.xview)
    scroll2.pack(side=tk.BOTTOM, fill=tk.X, expand=True, anchor="ne")

    scatter = FigureCanvasTkAgg(figure, fram2)
    scatter.get_tk_widget().pack(fill='both', expand=True, padx=0, pady=0)
    canva.create_window((0, 0), window=fram2, anchor="center")
    canva.configure(yscrollcommand=scroll.set)
    canva.configure(xscrollcommand=scroll2.set)

    fram.bind(
        "<Configure>",
        lambda e: canva.configure(
            scrollregion=canva.bbox("all")
        )
    )
    #------------------------


    ax1 = figure.add_subplot(321)
    ax1.plot(df1['year'], df1['personal'], color='red')
    figure.tight_layout(pad=5)  # add space betwenn figure
    ax1.legend([''])
    ax1.set_xlabel('valeur de personals')
    ax1.set_title('ev de personal ')

    ax1.get_cursor_data(self)

    #-------------------------
    ax2 = figure.add_subplot(322)
    ax2.plot(df2['year'], df2['value'], color='red')
    ax2.legend([''])
    ax2.set_xlabel('valeur BSA')
    ax2.set_title('Evolutiion des valeurs BSA depuis 1990 ')

    #---------------------------

    ax3 = figure.add_subplot(323)
    ax3.plot(df3['year'], df3['percentage_of_total_population'], color='red')
    ax3.legend([''])
    ax3.set_xlabel("taux d'imigration")
    ax3.set_title("Evolution des taux d'imigratan exprimé en %  ")
    #---------------------------

    #--------------------------
    ax4 = figure.add_subplot(324)
    ax4.plot(df4['year'], df4['value'], color='green')
    ax4.legend([''])
    ax4.set_xlabel(" % utilisation internet")
    ax4.set_title("Evolution utulisation internet  exprimé en %  ", fontsize=10)
    #-------------------------

    #------------------------
    ax5 = figure.add_subplot(325)
    ax5.scatter(df5['year'], df5['value'], color='g')
    ax5.legend(['PIB'])
    ax5.set_xlabel('vlauer de pib')
    ax5.set_title('ev de pib depuis 1990')
    #------------------------
    crs1 = mplcursors.cursor(ax1, hover=True)
    crs2 = mplcursors.cursor(ax2, hover=True)
    crs3 = mplcursors.cursor(ax3, hover=True)
    crs4 = mplcursors.cursor(ax4, hover=True)
    crs5 = mplcursors.cursor(ax5, hover=True)
    '''
    crs1.connect("add", lambda sel: sel.annotation.set_text(
    'Année : {}, valeur : {}'.format(sel.target[0], sel.target[1])))
    crs2.connect("add", lambda sel: sel.annotation.set_text(
        'Point {},{}'.format(sel.target[0], sel.target[1])))
    crs3.connect("add", lambda sel: sel.annotation.set_text(
        'Point {},{}'.format(sel.target[0], sel.target[1])))
    crs4.connect("add", lambda sel: sel.annotation.set_text(
        'Point {},{}'.format(sel.target[0], sel.target[1])))
    crs5.connect("add", lambda sel: sel.annotation.set_text(
        'Point {},{}'.format(sel.target[0], sel.target[1])))
    '''
    #---------------2 section ---------------------

    fram3 = tk.Frame(tab2)
    fram3.pack(fill='both', expand=True, padx=0, pady=0)
    myFont2 = font.Font(family='Helvetica', size=20, weight='bold')
    b2 = tk.Button(fram3, text='Courbes pour :' + format(', '.join(str)), borderwidth=0,command=lambda: hide_widget(str))
    b2['font'] = myFont2

    b2.pack()
    #fram --->fram 3
    #fram2 ---> fram 4
    #canvas--->canvas 2
    #figure --->figure 2
    canva2 = tk.Canvas(fram3)
    canva2.pack(fill='both', expand=True)
    fram4= tk.Frame(canva2)
    fram4.pack(fill='both', expand=True)
    figure2 = plt.Figure(figsize=(12, 12), dpi=100)
    scroll3 = Scrollbar(fram4, orient=VERTICAL, command=canva2.yview)
    scroll3.pack(side=tk.RIGHT, fill=tk.Y, expand=True, anchor="ne")

    scroll4 = Scrollbar(fram4, orient=HORIZONTAL, command=canva2.xview)
    scroll4.pack(side=tk.BOTTOM, fill=tk.X, expand=True, anchor="ne")

    scatter2 = FigureCanvasTkAgg(figure2, fram4)
    scatter2.get_tk_widget().pack(fill='both', expand=True, padx=0, pady=0)
    canva2.create_window((0, 0), window=fram4, anchor="center")
    canva2.configure(yscrollcommand=scroll3.set)
    canva2.configure(xscrollcommand=scroll4.set)

    fram3.bind(
        "<Configure>",
        lambda e: canva2.configure(
            scrollregion=canva2.bbox("all")
        )
    )
    # ------------------------

    ax6 = figure2.add_subplot(221)
    ax6.plot(df1['year'], df1['personal'], color='red')
    figure2.tight_layout(pad=5)  # add space betwenn figure
    ax6.legend([''])
    ax6.set_xlabel('valeur de personals')
    ax6.set_title('ev de personal ')


    # -------------------------
    ax7 = figure2.add_subplot(222)
    ax7.plot(df2['year'], df2['value'], color='red')
    ax7.legend([''])
    ax7.set_xlabel('valeur BSA')
    ax7.set_title('Evolutiion des valeurs BSA depuis 1990 ')

    # ---------------------------
    ax8 = figure2.add_subplot(223)
    ax8.plot(df4['year'], df4['value'], color='green')
    ax8.legend([''])
    ax8.set_xlabel(" % utilisation internet")
    ax8.set_title("Evolution utulisation internet  exprimé en %  ", fontsize=10)

    # ---------------------------

    # ------------------------





    root.mainloop()


