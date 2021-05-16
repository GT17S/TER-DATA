#Requete utilisé pour le fichier de bsa.py qui affiche les valeurs sur la map
Bsa_value = ('''select nicename,year,value as value from bsa,countries where country=%s ''')



#Requetes utilisé dans de bsa.py qui permet d'afficher les courbes des pays selectionnés
#sur la barre de recherche des le lancement de l'application.
Evolution_de_nombre_de_personels = ('''
            select personal,year
            from gmi g,countries s
            where g.country_id=s.id and s.nicename=%s
            order by year
            ''')

Evolution_des_valeurs_BSA_depuis_1990 = ('''
            select B.year , B.value
            from bsa B , countries C 
            where C.id = B.country_id 
                  and C.nicename=%s ''')

Evolution_des_taux_imigrants = ('''
            select I.year , I.percentage_of_total_population
            from imigration I  , countries C 
            where C.id = I.country_id 
                 and C.nicename=%s ''')


Evolution_utilisation_internet  = ('''
            select IP.year , IP.value
            from ipu IP  , countries C 
            where C.id = IP.country_id 
            and C.nicename=%s ''')


Evolution_PIB_depuis_1990 = ('''
            SELECT P.value::numeric(10,2) as value  , P.year as year
            FROM countries C , countries_in_regions CIR , world_regions WR , pib P 
            where  
            CIR.region_id = WR.id  AND CIR.country_id = C.id AND P.country_id = C.id and C.nicename=%s''')


Evolution_des_taux_de_piratage_de_logiciel= ('''
               select B.year , B.index
               from BSA B  , countries C 
               where C.id = B.country_id and C.nicename=%s ''')

#____________________________________
#Evolution de Régime Politique de pays
colonise = ('''select PL.year , PL.value
               from political_regime PL  , countries C 
               where C.id = PL.country_id and C.nicename=%s and PL.value <=-20 ''')

autocracie = ('''select PL.year , PL.value
                  from political_regime PL  , countries C 
                  where C.id = PL.country_id and C.nicename=%s and PL.value between -10 and -6 ''')

closed_anocracie = ('''select PL.year , PL.value
                  from political_regime PL  , countries C 
                  where C.id = PL.country_id and C.nicename=%s and PL.value between -5 and 0 ''')

open_anocracie = ('''select PL.year , PL.value
                  from political_regime PL  , countries C 
                  where C.id = PL.country_id and C.nicename=%s and PL.value between 1 and 5''')

democracie = ('''select PL.year , PL.value
                      from political_regime PL  , countries C 
                      where C.id = PL.country_id and C.nicename=%s and PL.value between 6 and 10''')
#_____________________________________

Nombre_de_serveurs_securise = ('''
               select SS.year , SS.value
               from serveur_securise SS  , countries C 
               where C.id = SS.country_id and  C.nicename=%s ''')


Taux_de_chomage = ('''select S.year , S.value
               from sjr S , countries C 
               where C.id = S.country_id  and  C.nicename=%s ''')


Acces_electricite = ('''select AE.year , AE.value
              from acces_electricite AE  , countries C 
              where C.id = AE.country_id and  C.nicename=%s ''')

