import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input ,Output
import plotly.express as px
import pandas as pd
import Database.conxion as cx
import app

#----------------------------------
test1 = pd.read_sql_query('''SELECT C.name as name  , P.value::numeric(10,2) as value  , P.year as year ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , pib P  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id order by C.name''',cx.conn)
#----------------------------------

#----------------------------------
test2 = pd.read_sql_query('''SELECT C.name as name  , I.percentage_of_total_population as value  , I.year as year ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , Imigration I 
where CIR.region_id = WR.id  AND CIR.country_id = C.id AND I.country_id = C.id order by C.name''',cx.conn)
#-----------------------------------
#-----------------------------------
test3= pd.read_sql_query('''SELECT C.name as name  , S.year as year , S.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , sjr S where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND S.country_id = C.id order by C.name ''',cx.conn)
#-----------------------------------

#----------------------------------
test4 =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.personal as personal ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''',cx.conn)
#----------------------------------

#----------------------------------
test5 =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.expenditure as expenditure ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''',cx.conn)
#----------------------------------

#----------------------------------
test6 =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.weapons as weapons ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''',cx.conn)
#----------------------------------

#----------------------------------
test7 =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.score as score ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''',cx.conn)
#-----------------------------------

#----------------------------------
test8 =pd.read_sql_query(''' SELECT C.name as name  , H.year as year , H.count as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , homicides H where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND H.country_id = C.id order by C.name  ''',cx.conn)
#-----------------------------------

#----------------------------------
test9 =pd.read_sql_query(''' SELECT C.name as name  , AE.year as year , AE.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , acces_electricite AE where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND AE.country_id = C.id order by C.name  ''',cx.conn)
#-----------------------------------

#----------------------------------
test10 =pd.read_sql_query('''  SELECT C.name as name  , IP.year as year , IP.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , IPU IP where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND IP.country_id = C.id order by C.name ''',cx.conn)
#-----------------------------------
#----------------------------------
test11 =pd.read_sql_query(''' SELECT C.name as name  , SS.year as year , SS.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , serveur_securise SS where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND SS.country_id = C.id order by C.name ''',cx.conn)
#-----------------------------------

test12 =pd.read_sql_query('''SELECT C.name as name  , B.year as year , B.index as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR ,BSA B where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND B.country_id = C.id order by C.name''',cx.conn)
#-----------------------------------


all_continent = test1.continent.unique()

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
        mask = test12.continent.isin(all_continent)
        fig = px.scatter(test12[mask],
                      x="year", y="value", color='name', title="Evolution  des taux de piratage de logiciel exprimé en %")
        return fig

    elif (donnee=="Taux Imigration"):
        mask = test2.continent.isin(all_continent)
        fig = px.line(test2[mask],
         x = "year", y = "value", color = 'name',title = "Evolution des taux d'imigration exprimé en % ")
        return  fig

    elif (donnee=="Taux de Chomage"):
        mask = test3.continent.isin(all_continent)
        fig = px.line(test3[mask],
                      x="year", y="value", color='name', title="Evolution  taux de chomage exprimé en  %")
        return fig
    elif (donnee=="Pourcentage Utilisation Internet"):
        mask = test10.continent.isin(all_continent)
        fig = px.line(test10[mask],
                      x="year", y="value", color='name', title="Evolution utulisation internet  exprimé en %  ")
        return fig

    elif (donnee == "Military Personal Index Score"):
        mask = test4.continent.isin(all_continent)
        fig = px.line(test4[mask],
                      x="year", y="personal", color='name', title=" Evolution du Personnel Militaire ")
        return fig
    elif (donnee == "Military Expenditure Index Score"):
        mask = test5.continent.isin(all_continent)
        fig = px.scatter(test5[mask],
                      x="year", y="expenditure", color='name', title=" dépense militaire exprimé en Milliards de dollar ")
        return fig
    elif (donnee == "GMI Score"):
        mask = test7.continent.isin(all_continent)
        fig = px.scatter(test7[mask],
                      x="year", y="score", color='name', title=" GMI Score  ")
        return fig

    elif (donnee == "Heavy Weapons Index Score"):
        mask = test6.continent.isin(all_continent)
        fig = px.scatter(test6[mask],
                      x="year", y="weapons", color='name', title=" GMI Score  ")
        return fig

    elif (donnee == "Nombre Homicides"):
        mask = test8.continent.isin(all_continent)
        fig = px.scatter(test8[mask],
                         x="year", y="value", color='name', title=" Nombre Homicides  ")
        return fig

    elif (donnee == "Nombre Serveur Securisé"):
        mask = test11.continent.isin(all_continent)
        fig = px.scatter(test11[mask],
                         x="year", y="value", color='name', title=" Nombre Serveur Securisé par million d'habitants  ")
        return fig
    elif (donnee=="Evolution PIB"):
        mask = test1.continent.isin(all_continent)
        fig = px.scatter(test1[mask],
                      x="year", y="value", color='name', title="Evolution  PIB ")
        return fig
    elif (donnee == "Acces électricité"):
        mask = test9.continent.isin(all_continent)
        fig = px.scatter(test9[mask],
                         x="year", y="value", color='name', title="Acces électricité exprimé en % ")
        return fig

    return ""