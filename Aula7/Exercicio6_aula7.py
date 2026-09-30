produtos = ["Arroz", "Feijão", "Leite", "Café"]
quantidades = [15, 7, 4, 20]
reposicao = []
for i in range(len(produtos)):
    if quantidades[i] < 10:
        reposicao.append(produtos[i])

print(reposicao)