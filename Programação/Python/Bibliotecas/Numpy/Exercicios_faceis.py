# 1️⃣ Crie um array de zeros com tamanho 10 e substitua o quinto elemento por 100.
# 2️⃣ Gere um array de números pares de 2 a 20.
# 3️⃣ Crie uma matriz identidade 3x3 (com 1 na diagonal principal e 0 no restante).
# 4️⃣ Crie um array de 10 números aleatórios inteiros entre 1 e 50.
# 5️⃣ Inverta a ordem dos elementos de um array.
# 6️⃣ Encontre o índice do valor máximo e mínimo em um array.
# 7️⃣ Crie um array de 10 elementos igualmente espaçados entre 0 e 1.
# 8️⃣ Multiplique dois arrays A e B elemento por elemento.

import numpy as np

# 1️⃣ Crie um array de zeros com tamanho 10 e substitua o quinto elemento por 100.
arr_1 = np.zeros(10)
arr_1[4] = 100
print("Array de zeros com o quinto elemento substituído por 100:", arr_1)

# 2️⃣ Gere um array de números pares de 2 a 20.
arr_2 = np.arange(2, 21, 2)
print("Array de números pares de 2 a 20:", arr_2)

# 3️⃣ Crie uma matriz identidade 3x3 (com 1 na diagonal principal e 0 no restante).
matrix_1 = np.eye(3)
print("Matriz identidade 3x3:", matrix_1)

# 4️⃣ Crie um array de 10 números aleatórios inteiros entre 1 e 50.
arr_3 = np.random.randint(1, 50, 10)
print("Array de 10 números aleatórios inteiros entre 1 e 50:", arr_3)

# 5️⃣ Inverta a ordem dos elementos de um array.
arr_4 = np.array([1, 2, 3])
arr_4_inv = arr_4[::-1]
print("Array invertido:", arr_4_inv)

# 6️⃣ Encontre o índice do valor máximo e mínimo em um array.
arr_5 = np.random.randint(1, 50, 10)
arr_5_max = np.argmax(arr_5)
arr_5_min = np.argmin(arr_5)
print("Índice do valor máximo:", arr_5_max)
print("Índice do valor mínimo:", arr_5_min)

# 7️⃣ Crie um array de 10 elementos igualmente espaçados entre 0 e 1.
arr_6 = np.linspace(0, 1, 10)
print("Array de 10 elementos igualmente espaçados entre 0 e 1:", arr_6)

# 8️⃣ Multiplique dois arrays A e B elemento por elemento.
arr_7 = np.array([7, 8, 9])
arr_8 = np.array([4, 5, 6])
arr_result = arr_7 * arr_8
print("Multiplicação elemento por elemento entre dois arrays:", arr_result)