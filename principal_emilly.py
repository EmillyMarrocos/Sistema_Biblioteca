from conexao import connect
from funcao import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

mydb.close()
