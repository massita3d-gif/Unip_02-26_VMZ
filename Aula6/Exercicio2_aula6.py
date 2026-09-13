def formatar_codigo(codigo,tamanho):
    while len(codigo) < tamanho:
        codigo = "0"+codigo
    while len(codigo)>tamanho:
        print("O CODIGO E MAIOR QUE O DESEJADO!")
        codigo=str(input("DIGITE NOVAMENTE O CODIGO: "))
    print("CODIGO: ",codigo)
tamanho=int(input("DIGITE O TAMANHO DESEJADO: "))
codigo=str(input("DIGITE O CODIGO DESEJADO: "))
formatar_codigo(codigo,tamanho)
