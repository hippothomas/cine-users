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


if __name__ == '__main__':
    app.run(debug=True)
