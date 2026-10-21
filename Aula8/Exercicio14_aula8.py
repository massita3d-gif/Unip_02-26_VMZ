produtos = {"Notebook": 3500.0,"Celular": 2200.0,"Tablet": 1800.0,"Smartwatch": 1200.0}
maior_preco = 0
produto_mais_caro = ""
for produto, preco in produtos.items():
    if preco > maior_preco:
        maior_preco = preco
        produto_mais_caro = produto
print(produto_mais_caro)
print(maior_preco)