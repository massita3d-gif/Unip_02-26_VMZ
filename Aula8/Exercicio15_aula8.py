catalogo = {"P01": "Teclado", "P02": "Mouse", "P03": "Monitor"}
invertido = {}
for codigo, produto in catalogo.items():
    invertido[produto] = codigo
print(invertido)