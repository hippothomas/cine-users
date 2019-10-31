# cine-users

## Installation
Pour le bon fonctionnement du programme, il vous faut installer :<br>
```
pip install mysql-connector
pip install flask
pip install flask_restplus
pip install requests
```

Il faut ensuite importer le script SQL dans votre base de donnée puis changer les informations de connections présentes dans le main.py si besoin.

## Utilisation
- ```/users/``` : affiche tout les utilisateurs
- ```/user/<id>``` : affiche un utilisateur en fonction de l'id