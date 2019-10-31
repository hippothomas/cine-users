import requests


class UserTest:
    def UsersTest(self):
        r = requests.get('http://127.0.0.1:5000/users')

        if r.status_code == 200:
            print("UsersTest(): Test réussi")
        else:
            print("UsersTest(): Echec")

    def UserTest(self, id):
        r = requests.get('http://127.0.0.1:5000/user/' + str(id))

        if r.status_code == 200:
            print("UsersTest(): Test réussi")
        else:
            print("UsersTest(): Echec")


if __name__ == '__main__':
    ut = UserTest()

    ut.UsersTest()  # Réussite
    ut.UserTest(1)  # Réussite
    ut.UserTest(1000)  # Echec
