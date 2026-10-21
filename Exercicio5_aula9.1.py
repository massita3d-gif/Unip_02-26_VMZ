import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db"
)
def consultar_funcionarios():
    cursor = conexao.cursor()
    sql = """
    SELECT * FROM funcionarios
    WHERE salario > %s
    """
    cursor.execute(sql, (5000,))
    resultados = cursor.fetchall()
    for funcionario in resultados:
        print(funcionario)
    cursor.close()
consultar_funcionarios()