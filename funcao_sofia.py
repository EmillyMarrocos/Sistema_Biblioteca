<<<<<<<< HEAD:funcao_emilly.py
from conexao_emilly import connect
========
from conexao_sofia import connect
>>>>>>>> 5a74e2329df1ec7500086e16a278096dc0de8af5:funcao_sofia.py

def insert(mydb, titulo, autor):
    mycursor = mydb.cursor()

    sql = "INSERT INTO livros (titulo, autor) VALUES (%s, %s)"
    val = (titulo, autor)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()