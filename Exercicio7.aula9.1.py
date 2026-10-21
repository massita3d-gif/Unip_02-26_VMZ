import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db"
)
def excluir_funcionario(id_funcionario):
    cursor = conexao.cursor()
    sql = """
    DELETE FROM funcionarios
    WHERE id = %s
    """
    cursor.execute(sql, (id_funcionario,))
    conexao.commit()
    print("Funcionário excluído!")
    cursor.close()
excluir_funcionario(1)
