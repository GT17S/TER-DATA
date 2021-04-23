import matplotlib.pyplot as plt
import geopandas as gpd
from descartes import PolygonPatch
import pandas as pd
test2=pd.read_sql_query('''select nicename,year,value as value from bsa,countries where country=nicename ''',cx.cnx)

def plotCountryPatch( axes, country_name, fcolor ):
    # plot a country on the provided axes
    nami = test2[test2.nicename == country_name]
    namigm = nami.__geo_interface__['features']  # geopandas's geo_interface
    namig0 = {'type': namigm[0]['geometry']['type'], \
              'coordinates': namigm[0]['geometry']['coordinates']}
    axes.add_patch(PolygonPatch( namig0, fc=fcolor, ec="black", alpha=0.85, zorder=2 ))

ax2 = test2.plot( figsize=(8,4), edgecolor=u'gray', cmap='Set2' )


plt.ylabel('Latitude')
plt.xlabel('Longitude')

#ax2.axis('scaled')
plt.show()