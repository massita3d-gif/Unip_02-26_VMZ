import numpy as np
vendas = np.array([
    [15, 22, 13],
    [44, 20, 2] ])
total_vendedores = np.sum(vendas, axis=1)
print(total_vendedores)