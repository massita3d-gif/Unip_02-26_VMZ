import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db")
def inserir_funcionario(nome, cargo, salario, data_admissao):
    cursor = conexao.cursor()
    sql = """
    INSERT INTO funcionarios
    (nome, cargo, salario, data_admissao)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, cargo, salario, data_admissao)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
inserir_funcionario(
    "Carlos",
    "Gerente",
    6000,
    "2026-10-21"
)