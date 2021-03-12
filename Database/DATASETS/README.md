# Importation des données
L'importation des données c'est faite de la méme maniere comme proposer dans le dépot initial.

##Exemple d'importation 
Les données initiales se trouvent dans le fichier [API_IT.NET.USER.ZS_DS2_en_csv_v2_2055777.csv] se trouvant dans le lien donnée
https://data.worldbank.org/indicator/IT.NET.USER.ZS.

## Traitement des fichiers 
Pour faciliter l'intégration dans un SGBDR,nos  fichiers  ont  été transformé (avec l'utile de python).
Les mises en forme ont été supprimées et les données annuelles ont été placées les unes à la suite des autres.

Les résultats  se  trouvent  dans le fichiers suivants :
  * [ICT_USAGE_import.csv](./ICT_USAGE_import.csv) 
  * [pib_import.csv](./pib_import.csv)

## Importation des données

### Création et peuplement des tables de données
 Ces 2 fichiers  [ICT_USAGE_import.csv](./ICT_USAGE_import.csv) et [pib_import.csv](./pib_import.csv) ont été 
utilisés comme source de donnéés pour un SGBDR .

Ces fichiers sont utilisés comme source de données dans les scripts d'importations :
* [ipu.sql](ipu.sql)
* [pib.sql](pib.sql)
