precos={"Camisa":50.0,"Calca":120.0,"Meia":15.0}
quantidade={"Camisa":2,"Calca":1,"Meia":3}
total=0
for produto in precos:
    total = total + precos[produto] * quantidade[produto]
print(f"O VALOR TOTAL DO PEDIDO E: {total:.2f}")