clientes = [("Ana", "SP"), ("Carlos", "RJ"), ("Pedro", "SP"), ("Maria", "MG")]
por_cidade = {}
for nome, cidade in clientes:
    if cidade in por_cidade:
        por_cidade[cidade].append(nome)
    else:
        por_cidade[cidade] = [nome]
print(por_cidade)