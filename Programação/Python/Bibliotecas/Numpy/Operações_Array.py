import numpy as np

a = np.cos(0)

print(a) 
print(np.pi)
print(np.inf)
print(np.nan)

print("\n-------------------\n")

a_1 = np.array([1,2,3])
a_2 = np.array([[4,5,6]])

print(a_1 + a_2)
print(a_1 + 5)
print(a_1 * 10)
print(a_1 * a_2) #Multiplicação de matriz não matematicamente
print("\n-------------------\n")
print(a_2.dot(a_1)) #Multiplicação de matriz matematicamente