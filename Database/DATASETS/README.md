# Importation des données
L'importation des données c'est faite de la méme maniere comme proposer dans le dépot initial.

##Exemple d'importation 
Les données initiales se trouvent dans le fichier [API_IT.NET.USER.ZS_DS2_en_csv_v2_2055777.csv] se trouvant dans le lien donnée
https://data.worldbank.org/indicator/IT.NET.USER.ZS.

## Traitement des fichiers 
Pour faciliter l'intégration dans un SGBDR,nos  fichiers  ont  été transformé (avec l'utile de python).
Les mises en forme ont été supprimées et les données annuelles ont été placées les unes à la suite des autres.

Le code utilisé pour la transformation:
   
    df_in = pd.read_csv('csv_original.csv')
    df_out = df_in.set_index(['Liste des colonnes à non transformé ']).stack().reset_index()
    df_out.columns = ['Liste des colonnes final ']
    df_out.to_csv('outfile.csv', index=False)

Les résultats  se  trouvent  dans le fichiers suivants avec chaque lien ou le fichier CSV à été importer:
  * [ICT_USAGE_import.csv](./ICT_USAGE_import.csv) [lien ici](https://data.worldbank.org/indicator/IT.NET.USER.ZS)
  * [pib_import.csv](./pib_import.csv) [lien ici](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)
  * [serveur_securise_import](./serveur_securise_import.csv) [lien ici](https://data.worldbank.org/indicator/IT.NET.SECR.P6)
  * [political-regime.csv](./political-regime.csv) [lien ici](https://ourworldindata.org/democracy#world-maps-of-political-regimes-over-200-years)
  * [sans_job_import.csv](./sans_job_import.csv) [lien ici](https://www.macrotrends.net/countries/ranking/unemployment-rate)
  * [imigration.csv](./imigration.csv) [lien ici](https://www.macrotrends.net/countries/ranking/immigration-statistics)
  * [acces_electricite_import.csv](./acces_electricite_import.csv) [lien ici](https://www.macrotrends.net/countries/ranking/electricity-access-statistics)

## Importation des données

### Création et peuplement des tables de données
 Les fichiers  *.csv ont été 
utilisés comme source de donnéés pour un SGBDR .

Ces fichiers sont utilisés comme source de données dans les scripts d'importations :
* [ipu.sql](IPU.sql)
* [pib.sql](pib.sql)
* [serveur.sql](serveur.sql)
* [political-regime.sql](political-regime.sql)
* [sans_job.sql](sans_job.sql)
* [imigration.sql](imigration.sql)
* [acces_electricite.sql](./acces_electricite.sql)

