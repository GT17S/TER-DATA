import mplcursors as mplcursors
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

connection = psycopg2.connect(database="TER",
                              user="postgres",
                              password="halliche",
                              host="localhost",
                          port=5432)
""""
cursor = connection.cursor()
cursor.execute("select * from countries")
row=cursor.fetchall()
for r in row:
    print(r)
cursor.close()
"""
test=pd.read_sql_query('''select avg(h.count)::numeric(10,2) as moyenne  ,h.year
from homicides h
group by h.year
order by h.year''',connection)
test1=pd.read_sql_query('''
select sum(personal) as personal,year
from gmi 
group by year 
order by year 
''',connection)

test.plot(kind="bar",x="year",y="moyenne",color='red')

plt.ylabel("la moyenne d'homicide par années")
plt.title("l'évolution d'homicide depuis 2000")

test1.plot(kind="line",x="year",y="personal")
plt.ylabel("nombres de personal")
plt.title("l'évolution de personal depuis 1990")
mplcursors.cursor(hover=True)


plt.show()




'''df = pd.DataFrame.from_dict(test, orient='index', dtype=None)'''
'''df.head()'''

'''
cursor = connection.cursor()
cursor.execute("select  count(year),year from gmi group by year;")
row=cursor.fetchall()
for r in row:
    print(test)
cursor.close()
'''
connection.close()