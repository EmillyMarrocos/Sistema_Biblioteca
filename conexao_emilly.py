import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_biblioteca"
    )
<<<<<<< HEAD
    return mydb
=======
    return mydb
>>>>>>> 5a74e2329df1ec7500086e16a278096dc0de8af5
