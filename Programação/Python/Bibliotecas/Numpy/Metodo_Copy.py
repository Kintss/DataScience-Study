import numpy as np

arr_1 = np.arange(8)
arr_2 = arr_1 # É o mesmo array porem em diferentes variaveis.

print(arr_1)
print(arr_2)
print(arr_2 is arr_1)

arr_3 = arr_1.copy() # Agora o array é outro objeto, porem identicos.
print(arr_3)
print(arr_3 is arr_1)