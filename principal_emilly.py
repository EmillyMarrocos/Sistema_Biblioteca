from conexao_emilly import connect
from funcao_emilly import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

<<<<<<< HEAD
mydb.close()
=======
mydb.close()
>>>>>>> 5a74e2329df1ec7500086e16a278096dc0de8af5
