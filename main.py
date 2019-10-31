from flask import Flask
from flask_restplus import Resource, Api
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

@api.route('/users')
class Users(Resource):
    def get(self):
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()

        res = {
            "user": []
        }
        for x in myresult:
            res["user"].append({"id": str(x[0]), "nom": str(x[1]), "prenom": str(x[2]), "age": str(x[3])})

        return res

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
                "age": str(myresult[0][3])
            }
            return res
        else:
            api.abort(404)


if __name__ == '__main__':
    app.run(debug=True)
