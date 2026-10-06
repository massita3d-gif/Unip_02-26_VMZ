estoque = {"Arroz": 50, "Feijão": 0, "Açúcar": 20, "Café": 0}
disponiveis = {}
for produto, quantidade in estoque.items():
    if quantidade > 0:
        disponiveis[produto] = quantidade
print(disponiveis)