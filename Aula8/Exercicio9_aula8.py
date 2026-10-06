erros = ["404", "500", "404", "403", "500", "404"]
contagem = {}
for erro in erros:
    if erro in contagem:
        contagem[erro] = contagem[erro] + 1
    else:
        contagem[erro] = 1
print(contagem)