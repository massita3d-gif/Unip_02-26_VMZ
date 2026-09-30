import numpy as np
pixels=np.array([
    [100,200,260],
    [50,240,120]
])
pixels_ajustados=np.clip(pixels+20,0,255) # o 20 adiciona em todos os termos, e o 0=min e 255=max
print(pixels_ajustados)