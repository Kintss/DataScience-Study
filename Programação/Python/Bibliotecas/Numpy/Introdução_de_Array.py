from time import time
import numpy as np

# inicio = time()

lista_1 = list(range(10**6))
# soma_1 = 0 

# for i in lista_1:
#     soma_1 += 1 

# fim = time()
# tempo_1 = fim - inicio


# print(soma_1)
# print(tempo_1)


inicio = time()

arr = np.array(lista_1, dtype = float)
soma_2 = arr.sum()

fim = time()
tempo_2 = fim - inicio 

print(soma_2)
print(tempo_2)