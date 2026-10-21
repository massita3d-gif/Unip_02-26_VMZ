import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db")
cursor = conexao.cursor()
sql = """
INSERT INTO funcionarios
(nome, cargo, salario, data_admissao)
VALUES (%s, %s, %s, %s)
"""
funcionarios = [
    ("Ana", "Analista", 4500, "2026-01-10"),
    ("Pedro", "Supervisor", 6500, "2026-02-15"),
    ("Maria", "Diretora", 9000, "2026-03-20")
]
cursor.executemany(sql, funcionarios)
conexao.commit()
print("Funcionários cadastrados!")
cursor.close()