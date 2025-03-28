import pandas as pd
import numpy as np

lista_a = ['a','a','b','c','a','d','c']
lista_b = list(range(7))

dic = {'string': lista_a, 'numero':lista_b}

df = pd.DataFrame(dic)

df2 = pd.DataFrame({'col1': np.arange(100)**2, 'col2':np.arange(100)*5})
# print(df2.head(10))
# print(df2.tail(7))
print(df2.mean())
print(df2.min())
print(df2.max())
print(df2.median())
print(df2.cumsum()['col1'])
print(df2['col2'].value_counts())
