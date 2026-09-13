def remover_diplicados(texto):
    resultado=""
    for letra in texto:
        if letra not in resultado:
            resultado+=letra
    print(resultado)
texto=(input("DIGITE O TEXTO: "))
remover_diplicados(texto)