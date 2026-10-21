import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="210925",
    database="empresa_db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cargo VARCHAR(50),
        salario DECIMAL(10,2),
        data_admissao DATE)
""")

print("Tabela funcionarios criada com sucesso!")

cursor.close()
conexao.close()
