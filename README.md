# Projet de recherche : contrefaçon de logiciels dans le monde. Evolution dans le temps et dans l’espace.
Le projet à pour but l’observation et formulation des hypothèses explicatives sur le piratage des  logiciels. L’analyse des données, leur traitement et leur visualisation sont des parties essentielles pour réaliser les enjeux de ce  projet, et tous cela en proposant une base de données de nature diverse (économie, politique, société…) puis de les croiser avec celle déjà donnée au départ « BSA ».

Ce projet est réalisé dans le cadre de l'UE TER en Master 1 Data Scale informatique à l'Université de Versailles Saint-Quentin en Yvelines, encadré par Mr Stéphane LOPES.

## Installation 
### Pré-requis
Pour assurer le bon fonctionnement du code réalisé et permettre sa compilation, un certain nombre d'outils  et  de bibliothèques doivent être présents sur la machine:

Pour obtenir le projet il suffit de le cloner avec la commande:
` git clone https://github.com/TER-Piratage/TER-DATA.git`

### IDE Pycharm
On vous recommande de télécharger  l’IDE Pycharm sur le site [Télécharger Pycharm IDE](https://www.jetbrains.com/fr-fr/pycharm/download/ ) 
Et cela afin de lancer le code réalisé.
### Python 3.9
Après le téléchargement de Pycharm et son installation, vous aurez besoin de télécharger [Python 3.9](https://www.python.org/downloads/) 
Et cela afin de pouvoir utiliser les bibliothèques et les scripts nécessaires pour interpréter le code python réaliser sur pycharm (il fait le mème travaille qu’un JDK dans Java)

### Installation des bibliothèques nécessaires :
 Avant de pouvoir lancer le main de code, on doit tout d’abord interpréteur le code, et ce code à besoins l’installation des bibliothèques nécessaires pour la bonne interprétation de ce dernier et de l’exécuter par la suite.
Cette installation se fait sur le terminal(bash) de l’IDE de pycharm de cette manière :
<br>pip install ‘’nombibliotheque’’
<br>Pour notre projet Python:
###### Dash  `pip install dash`
###### Matplotlib  `pip install matplotlib`
###### Plotly  `pip install plotly`
###### Pandas  `pip install pandas`
###### Tkinter   `pip install tk`
###### mplcursors   `pip install mplcursors`
###### psycopg2   `pip install psycopg2` 
<br>Pour notre fichier Excel :
###### ODBC   https://www.postgresql.org/ftp/odbc/

### Fichier de connection PostgreSQL avec Python3.9
Après avoir installé tous les outils nécessaires pour le bon fonctionnement du code de projet, vous devez accéder au fichier 
[conxion.py](./importation/Database/conxion.py) et ensuite mettre l'identifiant et le mot de passe saisie lors de l'installation de PostgreSQL,
et cela afin de pouvoir connecter Python avec la base de données.

## Données ajoutées dans la base de données
Le projet initialement était basé sur des liens donner par le chargé de ce projet afin de les traiter et de créer une version de qualité, compréhensible et concise pour les intégrer dans la bases de données.

Le lien suivant vous emmène vers le [README.md](./importation/Database/DATASETS/README.md)
des datasets qui explique la façon de traitement de données et comment les intégrer dans la base de donnée avec des scripts SQL et des fichiers CSV comme fichiers sources
de peuplement des tables.

## Utilisation

Une fois le code correctement compilé et exécuté l'utilisateur se retrouve devant l'interface principale depuis laquelle il peut commencer à visualiser et comparer
les différentes datasets issue des liens donner initialement lors de début de projet.


## Contribution
Seuls les membres de l'organisation pouvant actuellement prendre part à se projet et le maintenir.

Cependant une fois la date de dépôt dépassée, une pull request pertinente et correctement formulée sera toujours la bienvenue.

## License
Avant la remise du projet au responsable de l'UE, la licence de ce projet n'est pas encore définie et sera peut être amenée à changer.
