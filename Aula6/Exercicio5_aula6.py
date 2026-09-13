def maior_palavra(frase):
    palavras=frase.split()
    maior_palavra = palavras[0]
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra=palavra
    print("A MAIOR PALAVRA E: ",maior_palavra)
frase=str(input("DIGITE A FRASE: "))
maior_palavra(frase)