import numpy as np

a = np.arange(10)**2

print(a)
print(a[2])
print(a[:2])
print(a[2:])
print(a[::2])
print(a[-2])
print(a[2:8:2])


print("\n-------------------\n")

b = np.arange(20).reshape(4,5)**2

print(b)
print(b[1,1])
print(b[1,2:])
print(b[2:,3:])
print(b[2:,3:])


