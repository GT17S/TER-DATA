import conxion as cn
import pandas as pd



cursor = cn.cnx.cursor()

cursor.execute("CREATE TABLE pib ("
               "country text NOT NULL, iso3 char(3),year integer , value numeric"
               ")")
cursor.execute("ALTER TABLE pib"
 " ADD PRIMARY KEY (country, year);")

cn.cnx.commit()

