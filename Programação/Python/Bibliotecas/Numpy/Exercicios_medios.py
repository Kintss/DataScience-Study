import numpy as np

# 1️⃣ Dado o array x = np.array([10, 20, 30, 40, 50]), normalize os valores para ficarem entre 0 e 1.
x = np.array([10, 20, 30, 40, 50])
x_norm = (x - np.min(x)) / (np.max(x) - np.min(x))
print("Array normalizado:", x_norm)

# 2️⃣ Gere uma matriz 4x4 com números aleatórios entre 0 e 100 e encontre a média de cada linha.
matrix_1 = np.random.randint(0, 100, (4, 4))
print("Matriz 4x4 gerada:")
print(matrix_1)
print("Média por linha:", matrix_1.mean(axis=1))

# 3️⃣ Crie uma matriz 5x5 e substitua todos os valores da borda por 1 e o interior por 0 (como uma moldura).
matrix_2 = np.zeros((5, 5))
matrix_2[0] = 1
matrix_2[-1] = 1
matrix_2[:, 0] = 1
matrix_2[:, -1] = 1
print("Matriz 5x5 com bordas de 1 e interior de 0:")
print(matrix_2)

# 4️⃣ Crie uma matriz 5x5 com valores aleatórios e substitua todos os valores acima de 50 por 50.
matrix_3 = np.random.randint(0, 100, (5, 5))
matrix_3[matrix_3 > 50] = 50
print("Matriz 5x5 com valores acima de 50 substituídos por 50:")
print(matrix_3)

# 5️⃣ Gere uma matriz 6x6 e substitua a diagonal principal por 1.
matrix_4 = np.random.randint(0, 1000, (6, 6))
for i in range(len(matrix_4)):
    matrix_4[(i, i)] = 1
print("Matriz 6x6 com diagonal principal substituída por 1:")
print(matrix_4)

# 6️⃣ Encontre a média, mediana e desvio padrão de um array aleatório de tamanho 20.
arr_5 = np.random.randint(0, 100, 20)
arr_5_media = arr_5.mean()
arr_5_mediana = np.median(arr_5)
arr_5_dp = np.std(arr_5)
print("Média, mediana e desvio padrão do array aleatório:", arr_5_media, ", ", arr_5_mediana, ", ", arr_5_dp)

# 7️⃣ Dado um array x = np.array([1, 2, 3, 4, 5]), repita cada elemento 3 vezes.
x = np.array([1, 2, 3, 4, 5])
x_3 = x.repeat(3)
print("Array com cada elemento repetido 3 vezes:")
print(x_3)

# 8️⃣ Concatene dois arrays horizontalmente e verticalmente.
arr_6 = np.arange(5)
arr_7 = np.arange(5) * 2
arr_ver = np.vstack((arr_6, arr_7))
arr_hor = np.hstack((arr_6, arr_7))
print("Concatenação vertical:")
print(arr_ver)
print("Concatenação horizontal:")
print(arr_hor)