# cine-users
Microservice de gestion d'utilisateurs - Réalisé pour un projet en cours

## Installation
Pour le bon fonctionnement du programme, il vous faut installer :<br>
```
pip install mysql-connector flask flask_restplus requests passlib jwt
```
Il faut ensuite importer le script SQL dans votre base de donnée puis changer les informations de connections présentes dans le main.py si besoin.<br>

Il peux être nécéssaire en fonction de votre version de python, en cas d'erreur, de modifier le packet passlib dans le fichier ``` venv\Lib\site-packages\passlib\utils\__init__.py ``` - [voir le patch](https://github.com/PyTables/PyTables/issues/744)

## Utilisation
- ```/users``` : [GET] affiche tout les utilisateurs
- ```/users``` : [POST] enregistre un utilisateur (Retourne un code HTTP 200 si valide sinon 400)<br>
Paramètres:
```
{
    "lastName": "nom",
    "firstName": "prenom",
    "login": "utilisateur",
    "password": "motdepasse",
    "age": "age"
}
```
- ```/user/<id>``` : [GET] affiche un utilisateur en fonction de l'id
- ```/login``` : [GET] permet de vérifier si le token envoyer est valide (Retourne un code HTTP 200 si valide sinon 401) 
- ```/login``` : [POST] retourne un token JWT à utiliser pour les autres requêtes<br> 
Paramètres:
```
{
    "user": "utilisateur",
    "password": "motdepasse"
}
```
Le mot de passe par défaut est "pwd"