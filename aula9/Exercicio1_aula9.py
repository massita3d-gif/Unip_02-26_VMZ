import random
numeros=[]
while len(numeros) <6:
    numero=random.randint(1,60)
    if numero not in numeros:
        numeros.append(numero)
numeros.sort()
print("Numeros Sorteados:",numeros)
