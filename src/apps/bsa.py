from tkinter import Label, font

import mplcursors as mplcursors
import pandas as pd
from tkinter import *
import plotly.express as px
import self
import importation.Database.conxion as cx
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from src.apps import app
import importation.Database.Querries.BSAQuerries as BSArq

it=pd.read_sql_query('''select nicename from countries''',cx.conn)

layout = html.Div([
    html.Div([
        #dcc.Link('Navigate to "/"', href='/'),
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
    [Output('output_state', 'children')],
    [Output(component_id='the_graph', component_property='figure')],
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
                            title='Valeur BSA des différents pays du monde ', animation_frame='year',
                            )

        fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                          margin=dict(l=60, r=60, t=50, b=50))
        if num_clicks>=1:
            inche(val_selected)

        return ('Le pays est : "{}" '.format(val_selected), fig)

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
    #utilisation des requetes des courbes ici, pour creer les dataframes necessaire pour les afficher en courbes
    df1 = pd.read_sql_query(BSArq.Evolution_de_nombre_de_personels, cx.conn, params=str)
    df2 = pd.read_sql_query(BSArq.Evolution_des_valeurs_BSA_depuis_1990, cx.conn, params=str)
    df3 = pd.read_sql_query(BSArq.Evolution_des_taux_imigrants, cx.conn, params=str)
    df4 = pd.read_sql_query(BSArq.Evolution_utilisation_internet, cx.conn, params=str)
    df5 = pd.read_sql_query(BSArq.Evolution_PIB_depuis_1990, cx.conn, params=str)
    df6 = pd.read_sql_query(BSArq.Evolution_des_taux_de_piratage_de_logiciel, cx.conn, params=str)
    df7 = pd.read_sql_query(BSArq.colonise, cx.conn, params=str)
    df7_1 = pd.read_sql_query(BSArq.autocracie, cx.conn, params=str)
    df7_2 = pd.read_sql_query(BSArq.closed_anocracie, cx.conn, params=str)
    df7_3 = pd.read_sql_query(BSArq.open_anocracie, cx.conn, params=str)
    df7_4 = pd.read_sql_query(BSArq.democracie, cx.conn, params=str)
    df8 = pd.read_sql_query(BSArq.Nombre_de_serveurs_securise, cx.conn, params=str)
    df9 = pd.read_sql_query(BSArq.Taux_de_chomage, cx.conn, params=str)
    df10 = pd.read_sql_query(BSArq.Acces_electricite, cx.conn, params=str)

    # from matplotlib.figure import Figure

    root = tk.Tk()
    #root.geometry("1600x900")
    root.fullScreenState = False
    root.attributes("-fullscreen", root.fullScreenState)
    #root.resizable(width=0, height=0)
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Courbes pour :'+format(', '.join(str)))
    tabControl.pack(expand=1, fill="both")


    fram = tk.Frame(tab1)
    fram.pack(fill='both', expand=True, padx=0, pady=0)
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    b1 = tk.Button(fram, text='Courbes pour :'+format(', '.join(str)), borderwidth=0)#lambda hide widghet
    b1['font'] = myFont

    b1.pack()

    canva = tk.Canvas(fram)
    canva.pack(fill='both', expand=True)
    fram2 = tk.Frame(canva)
    fram2.pack(fill='both', expand=True)
    figure = plt.Figure(figsize=(16,22),dpi=100)
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

    #-------------------------
    ax1 = figure.add_subplot(526)
    ax1.plot(df1['year'], df1['personal'], color='m')
    figure.tight_layout(pad=8)  # add space betwenn figure
    ax1.set_xlabel('Années')
    ax1.set_ylabel('Valeur de personnels')
    ax1.set_title('Evolution de nombre de personnels ')
    ax1.get_cursor_data(self)
    # -------------------------

    #-------------------------
    ax2 = figure.add_subplot(522)
    ax2.plot(df2['year'], df2['value'], color='crimson')
    ax2.set_xlabel('Années')
    ax2.set_ylabel('Valeur BSA')
    ax2.set_title('Evolution des valeurs BSA à partir de 1990 ')
    #---------------------------

    # -------------------------
    ax3 = figure.add_subplot(523)
    ax3.plot(df3['year'], df3['percentage_of_total_population'], color='maroon')
    ax3.set_xlabel("Années")
    ax3.set_ylabel("Taux d'imigrants")
    ax3.set_title("Evolution des taux d'immigrants dans la population")
    #---------------------------

    #--------------------------
    ax4 = figure.add_subplot(524)
    ax4.plot(df4['year'], df4['value'], color='lime')
    ax4.set_xlabel("Années")
    ax4.set_ylabel("Utilisation internet en %")
    ax4.set_title("Evolution des taux  d'utilisation d'internet ")
    #-------------------------

    #------------------------
    ax5 = figure.add_subplot(525)
    ax5.plot(df5['year'], df5['value'], color='c')
    ax5.set_xlabel('Années')
    ax5.set_ylabel('Valeur de PIB')
    ax5.set_title('Evolution de pib à partir  de 1990')
    #------------------------

    # -----------------------------
    ax6 = figure.add_subplot(521)
    ax6.plot(df6['year'], df6['index'], color='gold')
    ax6.set_ylabel('Taux des Logiciels piratés')
    ax6.set_xlabel("Années")
    ax6.set_title('Evolution des taux de piratage de logiciels ')
    # ------------------------------------------

    # ----------------------------------------
    ax7 = figure.add_subplot(527)
    ax7.scatter(df7['year'], df7['value'], color='r', label='colonisé.')
    ax7.scatter(df7_1['year'], df7_1['value'], color='y', label='autocracie')
    ax7.scatter(df7_2['year'], df7_2['value'], color='c', label='closed anocracie')
    ax7.scatter(df7_3['year'], df7_3['value'], color='k', label='open anocracie')
    ax7.scatter(df7_4['year'], df7_4['value'], color='green', label='democracie')
    legend = ax7.legend(loc='upper left', shadow=True, fontsize='x-large', prop={'size': 7})
    ax7.set_ylabel('Regime Politique')
    ax7.set_xlabel("Années")
    ax7.set_title('Evolution du Régime Politique ')
    # ---------------------------------------

    # ---------------------------------------
    ax8 = figure.add_subplot(528)
    ax8.plot(df8['year'], df8['value'], color='plum')
    ax8.set_ylabel('Nombre serveur sécurisé ')
    ax8.set_xlabel("Années")
    ax8.set_title('Le nombre de serveur sécurisé par millions d’habitants')
    # --------------------------------------

    # ---------------------------------------
    ax9 = figure.add_subplot(529)
    ax9.plot(df9['year'], df9['value'], color='palegreen')
    ax9.set_ylabel('Taux de Chomage')
    ax9.set_xlabel("Années")
    ax9.set_title('Taux de chômage ')
    # ---------------------------------------

    # --------------------------------------
    ax10 = figure.add_subplot(5, 2, 10)
    ax10.plot(df10['year'], df10['value'], color='burlywood')
    ax10.set_ylabel('Accés électricité')
    ax10.set_xlabel("Années")
    ax10.set_title("Taux accès à l'électricité ")
    # --------------------------------------


    root.mainloop()