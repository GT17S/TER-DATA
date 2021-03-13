import conxion as cn
import pandas as pd


'''
cursor = cn.cnx.cursor()

cursor.execute("CREATE TABLE pib ("
               "country text NOT NULL, iso3 char(3),year integer , value numeric"
               ")")
cursor.execute("ALTER TABLE pib"
 " ADD PRIMARY KEY (country, year);")
'''
cursor = cn.cnx.cursor()
'''
cursor.execute("CREATE TABLE pib_import ("
               "country text NOT NULL, iso3 char(3),year integer , value numeric"
               ")")
'''
'''
df_in = pd.read_csv('PIB_PAR_Habitant.csv')
df_out = df_in.set_index(['Country Name','Country Code']).stack().reset_index()
df_out.columns = ['Country Name','Country Code', 'year','value']
df_out.to_csv('PIB_PAR_Habitant_final.csv', index=False)
'''
cursor.execute("copy pib_import from 'PIB_PAR_Habitant_final.csv' with (format csv);")

cn.cnx.commit()

