def contar_vogais_consoantes(texto):
    vogais=0
    consoantes=0
    texto=texto.upper()
    for letra in texto:
        if letra in "AEIOU":
            vogais += 1
        else:
            consoantes += 1
    print("EXISTEM:",vogais,"VOGAIS E", consoantes,"CONSOANTES")
texto=str(input("DIGITE O TEXTO DESEJADO:"))
contar_vogais_consoantes(texto)
    
