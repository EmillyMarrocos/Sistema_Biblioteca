from conexao_emilly import connect
from funcao_emilly import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

mydb.close()
