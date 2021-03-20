import matplotlib.pyplot as plt
import pandas as pd
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

df_in = pd.read_csv('sansjob.csv',error_bad_lines=False,delimiter=";")
#df_out=df_in.set_index('Country Name').stack().reset_index()
df_out = df_in.set_index(['Country Name']).stack().reset_index()
df_out.columns = ["Country Name",'year','value']
df_out.to_csv('sans_job_import.csv')


fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,10))
ax1.plot(test1['year'],test1['personal'])
ax1.set_title("l'évolution de personal depuis 1990")
ax1.set_ylabel("nombres de personal")
ax2.bar(test['year'],test['moyenne'],color='red')
ax2.set_title("l'évolution d'homicide depuis 2000")
ax2.set_ylabel("la moyenne d'homicide par années")
plt.show()

cx.cnx.close()