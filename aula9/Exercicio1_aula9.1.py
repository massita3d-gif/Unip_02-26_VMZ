import mysql.connector
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="210925"
    )
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE DATABASE empresa_db")
    print("Banco de dados criado ou já existente!")
    cursor.close()
    conexao.close()
except:
    print("OCORREU ALGUM ERRO, TENTEO NOVAMENTE")
