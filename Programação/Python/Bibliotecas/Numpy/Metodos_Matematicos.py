import numpy as np

arr_1 = np.arange(8).reshape(2,4)**2
print(arr_1)

print("\n-------------------\n")

arr_1[0][0] = 11
print(arr_1)

print("\n-------------------\n")

print(arr_1.max())
print(arr_1.max(axis=1))
print(arr_1.min())
print(arr_1.min(axis=1))

print("\n-------------------\n")

print(arr_1.argmax())
print(arr_1.argmin())

print("\n-------------------\n")

print(arr_1.sum(axis=1))
print(arr_1.mean())
print(arr_1.cumsum())
print(arr_1.cumprod())


