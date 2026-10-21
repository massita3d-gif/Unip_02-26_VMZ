import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db"
)
def reajustar_salario(id_funcionario, percentual):
    cursor = conexao.cursor()
    sql = """
    UPDATE funcionarios
    SET salario = ROUND(salario * (1 + %s / 100), 2)
    WHERE id = %s
    """
    cursor.execute(sql, (percentual, id_funcionario))
    conexao.commit()
    print("Salário atualizado!")
    cursor.close()
reajustar_salario(1, 10)