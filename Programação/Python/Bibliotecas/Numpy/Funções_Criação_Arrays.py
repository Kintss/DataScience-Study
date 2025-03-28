import numpy as np

print(np.zeros(6))
print(np.ones(6)*14)
print(np.eye(4))

print("\n-------------------\n")

arr_1 = np.arange(0, 5, 0.5)
print(arr_1)

arr_2 = np.linspace(0, 10, 5)
print(arr_2)
print(arr_2.size)

print("\n-------------------\n")

arr_3 = np.ones(8)
arr_4 = arr_3.reshape(2,4) # Não modifica o array original
arr_3.resize(2,4) # Modifica o array original
print(arr_3)
print(arr_4)

print("\n-------------------\n")

arr_5 = np.zeros(8)
arr_5.resize(2,4)

arr_6 = np.vstack((arr_5, arr_3)) # Incrementa o array na parte de baixo
arr_7 = np.hstack((arr_5, arr_3)) # Incrementa o array na lateral
print(arr_6)
print(arr_7)

