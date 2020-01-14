from flask import Flask, request
from flask_restplus import Resource, Api
from passlib.apps import custom_app_context as pwd_context
import jwt
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cine-users"
)
mycursor = mydb.cursor()

app = Flask(__name__)
api = Api(app,
          version="1.0.0",
          title="Cine-users",
          description="API d'authentification, et de récupération des utilisateurs"
         )
CORS(app, resources={r"/*": {"origins": "*"}})

login_ns = api.namespace('login', description='Opération d\'authentification et vérification de token')
user_ns = api.namespace('user', description='Actions sur les utilisateurs')

secret = 'U<CAPeR{*\(M_a"au>`]vYQ!Xi_bbdkJ3j9wX.O$-!{f*kBhT1@xe/D2}U#:3X+'

@login_ns.route('')
class Login(Resource):
    @login_ns.doc('Login()')
    def get(self):
        ''' Retourne le token de login '''
        if hasattr(request, 'authorization'):
            header = request.headers.get('Authorization')
            header = header.replace("Bearer ", "")
            try:
                user = jwt.decode(header, secret, algorithms=['HS256'])
            except:
                api.abort(401)

            mycursor.execute("SELECT count(*) FROM users WHERE login =  %s;", (str(user['login']),))
            myresult = mycursor.fetchone()

            if myresult[0] == 1:
                return {"message": "Token valide"}
            else:
                api.abort(401)
        else:
            api.abort(401)

    @login_ns.param('user', description='Nom de l\'utilisateur', type="string")
    @login_ns.param('pwd', description='Password de l\'utilisateur', type="string")
    def post(self):
        ''' Récupération du token de login '''
        user = request.json['user']
        pwd = request.json['password']

        mycursor.execute("SELECT id, password FROM users WHERE login =  %s;", (user,))
        myresult = mycursor.fetchall()

        if verify_password(pwd, myresult[0][1]):
            encoded = jwt.encode({'id': myresult[0][0], 'login': user}, secret, algorithm='HS256').decode('utf-8')
            return {"token": str(encoded)}
        else:
            api.abort(401)

@user_ns.route('s')
class Users(Resource):
    def get(self):
        ''' Retourne tous les utilisateurs '''
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()

        res = {
            "user": []
        }
        for x in myresult:
            res["user"].append({"id": str(x[0]), "nom": str(x[1]), "prenom": str(x[2]), "age": str(x[5])})

        return res

    @user_ns.param('nom', description='Nom de l\'utilisateur', type="string")
    @user_ns.param('prenom', description='Prénom de l\'utilisateur', type="string")
    @user_ns.param('login', description='Login de l\'utilisateur', type="string")
    @user_ns.param('pwd', description='Password de l\'utilisateur', type="string")
    @user_ns.param('age', description='Age de l\'utilisateur', type="int")
    def post(self):
        ''' Ajouter un utilisateur '''
        nom = request.json['lastName']
        prenom = request.json['firstName']
        login = request.json['login']
        pwd = pwd_context.hash(request.json['password'])
        age = request.json['age']

        if nom == "" or prenom == "" or login == "" or pwd == "" or age == "":
            api.abort(400)

        mycursor.execute("SELECT count(*) FROM users WHERE login =  %s;", (login,))
        myresult = mycursor.fetchone()

        if myresult[0] == 0:
            try:
                sql = "INSERT INTO users (lastname, firstname, login, password, age) VALUES (%s, %s, %s, %s, %s)"
                val = (nom, prenom, login, pwd, age)
                mycursor.execute(sql, val)

                mydb.commit()

                id = mycursor.lastrowid
            except:
                api.abort(400)
        else:
            api.abort(400)


@user_ns.route('/<id>')
class User(Resource):
    @user_ns.param('id', description='ID de l\'utilisateur', type="string")
    def get(self, id):
        ''' Retourne tous les utilisateurs '''
        mycursor.execute("SELECT * FROM users WHERE id = " + str(int(id)))
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            res = {
                "id": str(myresult[0][0]),
                "nom": str(myresult[0][1]),
                "prenom": str(myresult[0][2]),
                "age": str(myresult[0][5])
            }
            return res
        else:
            api.abort(404)


def verify_password(password, pwd):
    return pwd_context.verify(password, pwd)


if __name__ == '__main__':
    app.run(debug=True)
