import matplotlib.pyplot as plt
import pandas as pd
from plotly.validators.choropleth import _locationmode

from  Database import conxion as cx

test=pd.read_sql_query('''select avg(h.count)::numeric(10,2) as moyenne  ,h.year
from homicides h
group by h.year
order by h.year''',cx.cnx)
test1=pd.read_sql_query('''
select sum(personal) as personal,year
from gmi 
group by year 
order by year 
''',cx.cnx)
test2=pd.read_sql_query('''select nicename,year,value as value from bsa,countries where country=nicename ''',cx.cnx)
'''
df_in = pd.read_csv('sansjob.csv',error_bad_lines=False,delimiter=";")
#df_out=df_in.set_index('Country Name').stack().reset_index()
df_out = df_in.set_index(['Country Name']).stack().reset_index()
df_out.columns = ["Country Name",'year','value']
df_out.to_csv('sans_job_import.csv')
'''
'''
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,10))
ax1.plot(test1['year'],test1['personal'])
ax1.set_title("l'évolution de personal depuis 1990")
ax1.set_ylabel("nombres de personal")
ax2.bar(test['year'],test['moyenne'],color='red')
ax2.set_title("l'évolution d'homicide depuis 2000")
ax2.set_ylabel("la moyenne d'homicide par années")
plt.show()
cx.cnx.close()
'''
import json

with open('pays.json') as json_file:
    data = json.load(json_file)

import plotly.express as px

fig = px.choropleth(data_frame = test2,geojson=data, locations='nicename',color='value',locationmode='country names',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Regions with Positive Cases',animation_frame='year',
                    #labels={'value':'value bsa'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
config = dict({'scrollZoom': True})
fig.show(config=config)

'''
fig = px.scatter_geo(data_frame=test2,
    locations ="nicename",
locationmode='country names',
    color="value",
    # what is the size of the biggest scatter point
    size_max = 500,
    projection="natural earth",
    # range, important to keep the same range on all charts
    range_color=(0,1000),
    # columns which is in bold in the pop up
    hover_name = "nicename",
    # format of the popup not to display these columns' data
    title="International Tourism",
    animation_frame="year"
                     )
fig.update_geos(showcountries = True)
fig.show()
'''