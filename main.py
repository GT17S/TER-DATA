import dash  # (version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import pandas as pd  # (version 1.0.0)
import plotly.express as px
import psycopg2
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# print(px.data.gapminder()[:15])

connection = psycopg2.connect(database="Ter_Piratage",
                              user="postgres",
                              password="Touf+0615",
                              host="localhost",
                              port=5432)


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
it = pd.read_sql_query('''select nicename from countries''', connection)
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
                               connection)
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
    cursor = connection.cursor()
    t = ("SELECT id FROM countries WHERE nicename= %s "
         )

    # Execute cursor.
    test1 = ('''
    select personal,year
    from gmi g,countries s
    where g.country_id=s.id and s.nicename=%s
    ''')
    df1 = pd.read_sql_query(test1, connection, params=str)

    test2 = ('''select B.year , B.value
                from bsa B , countries C 
                 where C.id = B.country_id 
                and C.nicename=%s ''')

    df2 = pd.read_sql_query(test2, connection, params=str)

    test3 = ('''select I.year , I.percentage_of_total_population
                    from imigration I  , countries C 
                     where C.id = I.country_id 
                     and C.nicename=%s ''')

    df3 = pd.read_sql_query(test3, connection, params=str)

    test4 = ('''select IP.year , IP.value
                from ipu IP  , countries C 
                where C.id = IP.country_id 
                and C.nicename=%s ''')

    df4 = pd.read_sql_query(test4, connection, params=str)

    test5 = ('''SELECT P.value::numeric(10,2) as value  , P.year as year
    FROM countries C , countries_in_regions CIR , world_regions WR , pib P  where  
    CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id and C.nicename=%s''')

    df5 = pd.read_sql_query(test5, connection, params=str)


    import matplotlib

    matplotlib.use("TkAgg")
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure

    import tkinter as tk
    from tkinter import ttk

    LARGE_FONT = ("Verdana", 12)

    class Graphs(tk.Tk):

        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            tk.Tk.wm_title(self, "Graphes et courbes")

            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (StartPage, PageOne, PageTwo, PageThree, PageFour,PageFive):
                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Informations de pays choisi" , font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button = ttk.Button(self, text="Personnels de GMI par années",
                                command=lambda: controller.show_frame(PageOne))
            button.pack()

            button2 = ttk.Button(self, text="Valeur de BSA au fil des années",
                                 command=lambda: controller.show_frame(PageTwo))
            button2.pack()

            button3 = ttk.Button(self, text="Pourcentage des imigrants dans ce pays par années",
                                 command=lambda: controller.show_frame(PageThree))
            button3.pack()

            button4 = ttk.Button(self, text="Pourcentage des utilisateurs d'internet par années",
                                 command=lambda: controller.show_frame(PageFour))
            button4.pack()

            button5 = ttk.Button(self, text="Evolution de PIB par années",
                                 command=lambda: controller.show_frame(PageFive))
            button5.pack()

    class PageOne(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Personnels de GMI", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Retourner vers page principale",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            figure1 = Figure(figsize=(5, 5),dpi=100)
            figure1.supylabel("Valeur des personnels")
            figure1.supxlabel("Années")
            figure1.suptitle("Evolution de personnels")

            ax1 = figure1.add_subplot(111)
            ax1.plot(df1['year'], df1['personal'], 'r.-')

            canvas = FigureCanvasTkAgg(figure1, self)
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    class PageTwo(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Valeur de BSA", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Retourner vers page principale",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            figure1 = Figure(figsize=(5, 5),dpi=100)
            figure1.supylabel("Valeur")
            figure1.supxlabel("Années")
            figure1.suptitle("BSA value au fil des années")

            ax1 = figure1.add_subplot(111)
            ax1.plot(df2['year'], df2['value'], 'g.-')

            canvas = FigureCanvasTkAgg(figure1, self)
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    class PageThree(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Pourcentage de nombres d'imigrants dans ce pays", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Retourner vers page principale",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            figure1 = Figure(figsize=(5, 5),dpi=100)
            figure1.supylabel("Pourcentage des Immigrants")
            figure1.supxlabel("Années")
            figure1.suptitle("Pourcentage des immigrants au fil des années")

            ax1 = figure1.add_subplot(111)
            ax1.plot(df3['year'], df3['percentage_of_total_population'], 'b.-')

            canvas = FigureCanvasTkAgg(figure1, self)
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    class PageFour(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Pourcentage de nombres d'utilisateurs d'internet dans ce pays au fil des années", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Retourner vers page principale",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            figure1 = Figure(figsize=(5, 5),dpi=100)
            figure1.supylabel("Pourcentage d'usage d'internet")
            figure1.supxlabel("Années")
            figure1.suptitle("Pourcentage d'usage d'internet au fil des années")

            ax1 = figure1.add_subplot(111)
            ax1.plot(df4['year'], df4['value'], 'y.-')

            canvas = FigureCanvasTkAgg(figure1, self)
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    class PageFive(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Evolution de PIB depuis 1990", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Retourner vers page principale",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()

            figure1 = Figure(figsize=(5, 5),dpi=100)
            figure1.supylabel("Valeur de PIB")
            figure1.supxlabel("Années")
            figure1.suptitle("Evolution de PIB national de 1990")

            ax1 = figure1.add_subplot(111)
            ax1.plot(df5['year'], df5['value'], 'r.-')

            canvas = FigureCanvasTkAgg(figure1, self)
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    app = Graphs()
    app.mainloop()


if __name__ == '__main__':
    plt.switch_backend('agg')
    app.run_server(debug=True, use_reloader=False)



