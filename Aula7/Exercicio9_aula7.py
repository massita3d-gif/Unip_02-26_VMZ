VIP = {"Ana", "Carlos", "João"}
Geral = {"João", "Maria", "Pedro", "Carlos"}
exclusivos_geral = Geral - VIP
total_convidados = VIP | Geral
print("Somente Geral:", exclusivos_geral)
print("Total de convidados únicos:", len(total_convidados))