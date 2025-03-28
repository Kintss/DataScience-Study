import numpy as np

# 1️⃣ Função para retornar valores únicos de um array

def valorUnico(arr):
    return np.unique(arr)

arr_1 = np.array([1, 2, 3, 3, 4, 2])
print("Valores únicos:", valorUnico(arr_1))

# 2️⃣ Criando uma matriz 6x6 com valores aleatórios e ordenando as colunas individualmente

matrix_1 = np.random.randint(50, size=(6, 6))
matrix_1.sort(axis=0)  # Ordena cada coluna separadamente
print("Matriz ordenada por colunas:")
print(matrix_1)

# 3️⃣ Encontrar índices dos valores maiores que a média do array

def maioresMedia(arr):
    arr_media = arr.mean()  # Calcula a média do array
    indices = np.where(arr > arr_media)[0]  # Obtém índices onde os valores são maiores que a média
    return indices

arr2 = np.random.rand(100)
print("Índices dos valores maiores que a média:", maioresMedia(arr2))

# 4️⃣ Criar uma matriz 8x8 representando um tabuleiro de xadrez

tabuleiro = np.zeros((8, 8), dtype=int)
tabuleiro[1::2, ::2] = 1  # Preenche casas alternadas com 1
tabuleiro[::2, 1::2] = 1
print("Tabuleiro de xadrez:")
print(tabuleiro)

# 5️⃣ Encontrar valores duplicados em um array e suas posições

def encontrar_duplicatas(arr):
    valores, contagens = np.unique(arr, return_counts=True)
    duplicados = valores[contagens > 1]  # Filtra apenas valores duplicados

    # Mapeia os valores duplicados para suas posições no array
    posicoes = {int(valor): np.where(arr == valor)[0].tolist() for valor in duplicados}
    
    return posicoes

arr_3 = np.array([1, 2, 3, 2, 4, 5, 3, 6, 7, 1])
print(encontrar_duplicatas(arr_3))

# 6️⃣ Encontrar a submatriz 3x3 com maior soma em uma matriz 10x10

def encontrar_melhor_submatriz(matriz, tamanho=3):
    linhas, colunas = matriz.shape
    max_soma = float('-inf')
    melhor_submatriz = None

    # Percorre todas as possíveis submatrizes 3x3
    for i in range(linhas - tamanho + 1):
        for j in range(colunas - tamanho + 1):
            submatriz = matriz[i:i+tamanho, j:j+tamanho]
            soma_atual = np.sum(submatriz)

            if soma_atual > max_soma:
                max_soma = soma_atual
                melhor_submatriz = submatriz.copy()

    return melhor_submatriz, max_soma

np.random.seed(42)  # Para reprodutibilidade
dados = np.random.randint(0, 101, (10, 10))  # Gera matriz 10x10
melhor_submatriz, soma_maxima = encontrar_melhor_submatriz(dados)

print("Matriz 10x10:\n", dados)
print("\nMelhor submatriz 3x3 com maior soma:\n", melhor_submatriz)
print("\nSoma máxima:", soma_maxima)

# 7️⃣ Normalização Min-Max em uma matriz 5x5

def normalizar_min_max(matriz):
    min_val = np.min(matriz)
    max_val = np.max(matriz)
    
    if max_val == min_val:
        return np.zeros_like(matriz)  # Evita divisão por zero

    return (matriz - min_val) / (max_val - min_val)

np.random.seed(42)  # Para reprodutibilidade
matriz = np.random.randint(0, 101, (5, 5))
matriz_normalizada = normalizar_min_max(matriz)

print("Matriz original:\n", matriz)
print("\nMatriz normalizada:\n", matriz_normalizada)

# 8️⃣ Resolver um sistema de equações lineares Ax = b

A = np.array([[2, -1, 3], [1, 3, 2], [4, 1, -2]], dtype=float)
b = np.array([5, 10, -3], dtype=float)
x = np.linalg.solve(A, b)  # Resolve Ax = b

print("Solução do sistema (vetor x):")
print(x)
