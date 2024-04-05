from conexao_filipe import connect
from funcao_filipe import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

mydb.close()
