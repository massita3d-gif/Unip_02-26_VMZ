def num_linha_palavra():
    with open("dados.txt", "r") as arquivo:
        conteudo=arquivo.read()
    palavras=conteudo.split()
    linhas=conteudo.splitlines()
    print("Linhas:", len(linhas))
    print("Palavras:", len(palavras))
num_linha_palavra()