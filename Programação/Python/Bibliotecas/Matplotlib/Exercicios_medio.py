import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 1️⃣ Plote três funções no mesmo gráfico: y = sin(x), y = cos(x) e y = sin(x) * cos(x), com legendas e cores diferentes.
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = y1 *y2
# plt.plot(x, y1, color="red", linestyle="-", label="y = sin(x)")
# plt.plot(x, y2, color="green", linestyle="--", label="y = cos(x)")
# plt.plot(x, y3, color="blue", linestyle=":", label="y = sin(x) * cos(x)")
# plt.title("Gráfico de Três Funções", fontsize=16)
# plt.xlabel("Eixo X", fontsize=12)
# plt.ylabel("Eixo Y", fontsize=12)
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.legend(loc="upper right", fontsize=10)
# plt.show()

# 2️⃣ Crie um gráfico de dispersão com 100 pontos aleatórios, colorindo os pontos com base em uma terceira variável z (use np.random.rand para z).
# x = np.random.rand(100)
# y = np.random.rand(100)
# z = np.random.rand(100)
# plt.scatter(x, y, c=z, marker='s', cmap="viridis")
# plt.colorbar(label="Intensidade")
# plt.title("Gráfico de Dispersão")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()

# 3️⃣ Plote um gráfico de barras empilhadas para comparar as vendas trimestrais de 3 produtos ao longo de 4 trimestres (use dados fictícios).
# produtos = np.array(['A','B','C'])
# trimestres = np.array([1,2,3,4])
# vendas = np.array([
#     [10, 20, 30, 40],  
#     [15, 25, 35, 45], 
#     [5, 10, 15, 20]])
# plt.bar(trimestres, vendas[0], label=produtos[0], color='red')
# plt.bar(trimestres, vendas[1], bottom=vendas[0], label=produtos[1], color='green')
# plt.bar(trimestres, vendas[2], bottom=vendas[0] + vendas[1], label=produtos[2], color='blue')
# plt.title("Vendas Trimestrais por Produto", fontsize=16)
# plt.xlabel("Trimestres", fontsize=12)
# plt.ylabel("Vendas", fontsize=12)
# plt.xticks(trimestres)
# plt.grid(True, axis='y', linestyle="--", alpha=0.5)
# plt.legend(loc="upper right", fontsize=10)
# plt.show()

# 4️⃣ Crie um gráfico de contorno (contour plot) para a função z = sin(x) * cos(y), onde x e y variam de -π a π.
# x = np.linspace(- np.pi, np.pi, 100)
# y = np.linspace(- np.pi, np.pi, 100)
# X, Y = np.meshgrid(x,y )
# Z = np.sin(x) * np.cos(y)
# plt.contourf(X, Y, Z, levels=20, cmap='viridis')
# plt.colorbar(label="Valor de z")
# plt.contour(x, y, z, levels=20, colors='black', linewidths=0.1)
# plt.title("Gráfico de Contorno: z = sin(x) * cos(y)", fontsize=16)
# plt.xlabel("Eixo X", fontsize=12)
# plt.ylabel("Eixo Y", fontsize=12)
# plt.show()

# 5️⃣ Plote um gráfico de boxplot para comparar a distribuição de 4 conjuntos de dados aleatórios (use np.random.normal para gerar os dados).
# dados = [np.random.normal(0, 1, 100), np.random.normal(2, 1.5, 100), np.random.normal(-3, 0.5, 100) ,np.random.normal(1, 6, 100)]
# plt.boxplot(dados, labels=['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4'], patch_artist=True,
#             boxprops=dict(facecolor='lightblue', color='blue'),
#             medianprops=dict(color='red'))
# plt.title("Boxplot de Dados Aleatórios", fontsize=16)
# plt.xlabel("Grupos", fontsize=12)
# plt.ylabel("Valores", fontsize=12)
# plt.grid(True, axis='y', linestyle="--", alpha=0.5)
# plt.show()

# 6️⃣ Crie um gráfico 3D (superfície) para a função z = sin(sqrt(x^2 + y^2)), onde x e y variam de -5 a 5.

# 7️⃣ Plote um gráfico de área (stackplot) para mostrar a contribuição de 3 categorias ao longo do tempo (use dados fictícios).

# 8️⃣ Crie um gráfico interativo com dois sliders: um para ajustar a amplitude e outro para ajustar a frequência da função y = A * sin(fx), onde A e f são controlados pelos sliders.