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
api = Api(app)
secret = 'U<CAPeR{*\(M_a"au>`]vYQ!Xi_bbdkJ3j9wX.O$-!{f*kBhT1@xe/D2}U#:3X+'

@api.route('/login')
class Login(Resource):
    def get(self):
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

    def post(self):
        user = request.json['user']
        pwd = request.json['password']

        mycursor.execute("SELECT id, password FROM users WHERE login =  %s;", (user,))
        myresult = mycursor.fetchall()

        if verify_password(pwd, myresult[0][1]):
            encoded = jwt.encode({'id': myresult[0][0], 'login': user}, secret, algorithm='HS256').decode('utf-8')
            return {"token": str(encoded)}
        else:
            api.abort(401)

@api.route('/users')
class Users(Resource):
    def get(self):
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()

        res = {
            "user": []
        }
        for x in myresult:
            res["user"].append({"id": str(x[0]), "nom": str(x[1]), "prenom": str(x[2]), "age": str(x[5])})

        return res

    def post(self):
        nom = request.json['last-name']
        prenom = request.json['first-name']
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


@api.route('/user/<id>')
@api.doc(params={'id': 'ID de l\'utilisateur'})
class User(Resource):
    def get(self, id):
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

def verify_password(self, password, pwd):
    return pwd_context.verify(password, pwd)

if __name__ == '__main__':
    app.run(debug=True)
