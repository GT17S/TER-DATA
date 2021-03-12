# Importation des données
L'importation des données c'est faite de la méme maniere comme proposer dans le dépot initial.

##Exemple d'importation 
Les données initiales se trouvent dans le fichier [API_IT.NET.USER.ZS_DS2_en_csv_v2_2055777.csv] se trouvant dans le lien donnée
https://data.worldbank.org/indicator/IT.NET.USER.ZS.

## Traitement du fichier initial
Pour faciliter l'intégration dans un SGBDR, le fichier initial a été transformé (avec l'utile de python).
Les mises en forme ont été supprimées et les données annuelles ont été placées les unes à la suite des autres.

Le résultat se trouve dans le fichier "ICT_USAGE_import.csv".

## Importation des données
### Création des tables

####Table d'usage d'internet par population dans le monde
La création de cette table se trouvent dans les scripts `SQL` :
* [ipu.sql]

### Création et peuplement des tables de données
À partir du fichier [ICT_USAGE_import.csv] on crée et remplit comme source de données de la table [IPU] avec le script
* [ipu.sql]
