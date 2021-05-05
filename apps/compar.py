import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input ,Output
import plotly.express as px
import app
import Database.Querries.CompareQuerries as Crq



all_continent = Crq.Evolution_PIB.continent.unique()

all_options= ["Taux Piratage Logiciel","Taux Imigration","Taux de Chomage","Pourcentage Utilisation Internet","Military Personal Index Score","Military Expenditure Index Score","GMI Score","Heavy Weapons Index Score"
              ,"Nombre Homicides","Nombre Serveur Securisé","Evolution PIB","Acces électricité"]

layout = html.Div([
    html.H1('Vizualization des données', style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Pre(children="Type de donné à vizualiser ", style={"fontSize":"170%"}),
            dcc.Dropdown(
                id='pymnt-dropdown', value='Taux Piratage Logiciel', clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in all_options]
            )
        ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-map', figure={}),
])


@app.app.callback(
    Output(component_id='my-map', component_property='figure'),
    [Input(component_id='pymnt-dropdown', component_property='value')]
)
def display_value(donnee):
    if (donnee=="Taux Piratage Logiciel"):
        mask = Crq.Taux_de_piratage.continent.isin(all_continent)
        fig = px.scatter(Crq.Taux_de_piratage[mask],
                         x="year", y="value", color='name', title="Evolution  des taux de piratage de logiciel exprimé en %")
        return fig

    elif (donnee=="Taux Imigration"):
        mask = Crq.Taux_imigration.continent.isin(all_continent)
        fig = px.line(Crq.Taux_imigration[mask],
                      x = "year", y = "value", color = 'name', title = "Evolution des taux d'imigration exprimé en % ")
        return  fig

    elif (donnee=="Taux de Chomage"):
        mask = Crq.Taux_chomage.continent.isin(all_continent)
        fig = px.line(Crq.Taux_chomage[mask],
                      x="year", y="value", color='name', title="Evolution  taux de chomage exprimé en  %")
        return fig
    elif (donnee=="Pourcentage Utilisation Internet"):
        mask = Crq.Pourcentage_utulisation_internet.continent.isin(all_continent)
        fig = px.line(Crq.Pourcentage_utulisation_internet[mask],
                      x="year", y="value", color='name', title="Evolution utulisation internet  exprimé en %  ")
        return fig

    elif (donnee == "Military Personal Index Score"):
        mask = Crq.Military_personnal_index_score.continent.isin(all_continent)
        fig = px.line(Crq.Military_personnal_index_score[mask],
                      x="year", y="personal", color='name', title=" Evolution du Personnel Militaire ")
        return fig
    elif (donnee == "Military Expenditure Index Score"):
        mask = Crq.Military_expenditure_index_score.continent.isin(all_continent)
        fig = px.scatter(Crq.Military_expenditure_index_score[mask],
                         x="year", y="expenditure", color='name', title=" dépense militaire exprimé en Milliards de dollar ")
        return fig
    elif (donnee == "GMI Score"):
        mask = Crq.Gmi_score.continent.isin(all_continent)
        fig = px.scatter(Crq.Gmi_score[mask],
                         x="year", y="score", color='name', title=" GMI Score  ")
        return fig

    elif (donnee == "Heavy Weapons Index Score"):
        mask = Crq.Heavy_weapons_index_score.continent.isin(all_continent)
        fig = px.scatter(Crq.Heavy_weapons_index_score[mask],
                         x="year", y="weapons", color='name', title=" GMI Score  ")
        return fig

    elif (donnee == "Nombre Homicides"):
        mask = Crq.Nombre_homicides.continent.isin(all_continent)
        fig = px.scatter(Crq.Nombre_homicides[mask],
                         x="year", y="value", color='name', title=" Nombre Homicides  ")
        return fig

    elif (donnee == "Nombre Serveur Securisé"):
        mask = Crq.Nombre_de_serveurs_securise.continent.isin(all_continent)
        fig = px.scatter(Crq.Nombre_de_serveurs_securise[mask],
                         x="year", y="value", color='name', title=" Nombre Serveur Securisé par million d'habitants  ")
        return fig
    elif (donnee=="Evolution PIB"):
        mask = Crq.Evolution_PIB.continent.isin(all_continent)
        fig = px.scatter(Crq.Evolution_PIB[mask],
                         x="year", y="value", color='name', title="Evolution  PIB ")
        return fig
    elif (donnee == "Acces électricité"):
        mask = Crq.Acces_electricite.continent.isin(all_continent)
        fig = px.scatter(Crq.Acces_electricite[mask],
                         x="year", y="value", color='name', title="Acces électricité exprimé en % ")
        return fig

    return ""