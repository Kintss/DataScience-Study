import pandas as pd
import numpy as np

lista_a = [11,22,33,44,55]
lista_b = ['a','b','c','d','e']

arr = np.arange(10)**2

serie_1 = pd.Series(lista_a, index= lista_b)
# print(serie_1)

serie_2 = pd.Series(arr)
# print(serie_2)

dic1 = {'a':123, 'b':456, 'c': 789}

dic2 = {'coluna1':np.arange(10)*5, 'coluna2': np.arange(10)**2, 'coluna3': np.ones(10)}

df1 = pd.DataFrame(dic2)
print(df1)