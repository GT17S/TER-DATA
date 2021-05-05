import pandas as pd
import Database.conxion as cx

'''Requetes pour le fichier de comapar qui fait la comparaison sur la fenetre de comparaison apres avoir cliquer sur le lien de comparaison'''

#----------------------------------
Evolution_PIB = pd.read_sql_query('''SELECT C.name as name  , P.value::numeric(10,2) as value  , P.year as year ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , pib P  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id order by C.name''', cx.conn)
#----------------------------------

#----------------------------------
Taux_imigration = pd.read_sql_query('''SELECT C.name as name  , I.percentage_of_total_population as value  , I.year as year ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , Imigration I 
where CIR.region_id = WR.id  AND CIR.country_id = C.id AND I.country_id = C.id order by C.name''', cx.conn)
#-----------------------------------

#-----------------------------------
Taux_chomage= pd.read_sql_query('''SELECT C.name as name  , S.year as year , S.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , sjr S where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND S.country_id = C.id order by C.name ''', cx.conn)
#-----------------------------------

#----------------------------------
Military_personnal_index_score =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.personal as personal ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''', cx.conn)
#----------------------------------

#----------------------------------
Military_expenditure_index_score =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.expenditure as expenditure ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''', cx.conn)
#----------------------------------

#----------------------------------
Heavy_weapons_index_score =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.weapons as weapons ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''', cx.conn)
#----------------------------------

#----------------------------------
Gmi_score =pd.read_sql_query(''' SELECT C.name as name  , G.year as year , G.score as score ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , gmi G  where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND G.country_id = C.id order by C.name ''', cx.conn)
#-----------------------------------

#----------------------------------
Nombre_homicides =pd.read_sql_query(''' SELECT C.name as name  , H.year as year , H.count as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , homicides H where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND H.country_id = C.id order by C.name  ''', cx.conn)
#-----------------------------------

#----------------------------------
Acces_electricite =pd.read_sql_query(''' SELECT C.name as name  , AE.year as year , AE.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , acces_electricite AE where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND AE.country_id = C.id order by C.name  ''', cx.conn)
#-----------------------------------

#----------------------------------
Pourcentage_utulisation_internet =pd.read_sql_query('''  SELECT C.name as name  , IP.year as year , IP.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , IPU IP where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND IP.country_id = C.id order by C.name ''', cx.conn)
#-----------------------------------

#----------------------------------
Nombre_de_serveurs_securise =pd.read_sql_query(''' SELECT C.name as name  , SS.year as year , SS.value as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR , serveur_securise SS where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND SS.country_id = C.id order by C.name ''', cx.conn)
#-----------------------------------

Taux_de_piratage =pd.read_sql_query('''SELECT C.name as name  , B.year as year , B.index as value ,WR.parent as continent
FROM countries C , countries_in_regions CIR , world_regions WR ,BSA B where
CIR.region_id = WR.id  AND CIR.country_id = C.id AND B.country_id = C.id order by C.name''', cx.conn)
#-----------------------------------
