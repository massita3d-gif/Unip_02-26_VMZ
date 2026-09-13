def mascarar_cartao(numero_cartao):
    if len(numero_cartao) ==16:
        numero_cartao= "*"*12 +numero_cartao[-4:]
        print(numero_cartao)
    else:
        print("Numero do cartao invalido!")
numero_cartao=str(input("DIGITE O NUMERO DO CARTAO: "))
mascarar_cartao(numero_cartao)
     
