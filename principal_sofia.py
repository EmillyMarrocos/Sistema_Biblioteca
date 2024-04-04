from conexao_sofia import connect
from funcao_sofia import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

mydb.close()