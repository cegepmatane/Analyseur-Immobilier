# `Analyseur Immobilier`

# __Présentation du projet :__
Le but de ce projet est de créer un outil d'analyse d'immobilier à partir d'images et de textes. Il permettra de déterminer le prix d'un bien immobilier ainsi que ses caractéristiques. Il pourra aussi permettre de déterminer si un bien immobilier est surévalué ou sous-évalué.

La première partie du projet est réalisé dans le cadre du projet de spécialisation du Cégep de Matane sur un semestre. Il en résultera une preuve de concept pour le 24 février 2023 ainsi qu'un premier livrable le 4 avril 2023 qui ne contiendront qu'une petite partie du projet.

Ce projet sera poursuivi par la suite dans un cadre professionnel pour terminer le développement de l'outil et son déploiement.

# __Présentation du premier livrable :__
Cette version de base va d'abord être capable de reconnaître les caractéristiques d'un bien immobilier à partir d'une image. Il devra reconnaitre à quelle partie du bien immobilier l'image correspond (extérieur, intérieur, cuisine, chambre, etc.) et ensuite reconnaitre les caractéristiques de cette partie (nombre de pièces, nombre de salles de bain, etc.).
Pour ce faire, nous allons utiliser un dataset d'images d'immobilier et un modèle d'IA pré-entrainé. Nous allons ensuite utiliser ce modèle pour prédire les caractéristiques d'un bien immobilier à partir d'une image.

# __Présentation de l'outil final :__
L'outil sera composé de deux parties :
- Une partie web qui permet de récupérer les données d'un bien immobilier que l'utilisateur pourra saisir et de les envoyer au modèle d'IA.
- Une partie IA qui va recevoir les données et les traiter pour en faire une prédiction.

# __Technologies et librairies utilisées :__
- Python 3.10
- Tensorflow 2.11.0
- OpenCV 4.7.0
- Numpy 1.24.2
- Keras 2.11.0
- Matplotlib 3.6.3
- Sklearn 1.2.1
- PHP 8.0.13
