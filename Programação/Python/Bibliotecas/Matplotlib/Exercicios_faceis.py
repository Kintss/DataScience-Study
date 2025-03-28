import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# 1️⃣ Plote um gráfico de linha para y = x^2 com x de 0 a 10, adicionando título e rótulos nos eixos.
# x = np.arange(0, 11)
# y = x**2
# plt.plot(x, y)
# plt.plot(x, y, color="green", linestyle="--", marker="o", label="y = x²")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.legend()
# plt.title("Gráfico de linha")
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.show()

# 2️⃣ Gere 50 pontos aleatórios para x e y com np.random.rand e plote um gráfico de dispersão com marcadores quadrados.
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x, y, marker='s')
# plt.title("Gráfico de Dispersão")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()


# 3️⃣ Crie um gráfico de barras para as vendas ["A", "B", "C", "D", "E"] com valores [23, 45, 56, 78, 33], usando cores diferentes para cada barra.
# vendas = np.array(['A','B','C','D','E'])
# valores = np.array([23, 45, 56, 78, 33])
# plt.bar(vendas, valores, color=['red', 'green', 'blue', 'yellow', 'black'])
# plt.title("Vendas por Produto")
# plt.xlabel("Produtos")
# plt.ylabel("Vendas")
# plt.grid(True, axis='y', linestyle="--", alpha=0.5)
# plt.show()

# 4️⃣ Plote um gráfico de pizza para os votos ["Candidato A", "Candidato B", "Candidato C"] com valores [45, 30, 25], mostrando porcentagens e cores personalizadas.
# votos = np.array(["Candidato A", "Candidato B", "Candidato C"])
# valores = np.array([45, 30, 25])
# plt.pie(valores, labels=votos, autopct="%1.1f%%", colors=["red", "blue", "green"], shadow=True, explode=(0.1, 0, 0))
# plt.title("Distribuição de Votos")
# plt.show()

# 5️⃣ Gere 1000 números aleatórios com np.random.normal e plote um histograma com 30 bins, adicionando uma grade.
# nums = np.random.normal(100, 100, 1000)
# plt.hist(nums, bins=30, color="blue", edgecolor="black", alpha=0.7)
# plt.title("Histograma de Números Aleatórios", fontsize=16)
# plt.xlabel("Valores", fontsize=12)
# plt.ylabel("Frequência", fontsize=12)
# plt.grid(True, linestyle="--", alpha=0.3)
# plt.axvline(np.mean(nums), color="red", linestyle="--", label="Média")
# plt.legend()
# plt.show()

# 6️⃣ Plote y = sin(x) para x de 0 a 2π e adicione uma anotação com seta apontando para o ponto máximo.
# x = np.linspace(0, 2 * np.pi, 100)
# y = np.array(np.sin(x))
# plt.plot(x, y)
# plt.annotate("Máximo", xy=(np.pi/2, 1), xytext=(3, 0.9), arrowprops=dict(facecolor="red"), fontsize=12, color="red")
# plt.annotate("Mínimo", xy=(3*np.pi/2, -1), xytext=(2, -0.9), arrowprops=dict(facecolor="blue", shrink=0.05), fontsize=12, color="blue")
# plt.title("Gráfico de y = sin(x)")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()

# 7️⃣ Crie uma figura com 2 subplots: no primeiro, plote y = sin(x); no segundo, plote y = cos(x), adicionando títulos e rótulos para cada subplot.
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# fig, (ax1, ax2) = plt.subplots(2)
# ax1.plot(x, y1)
# ax1.set_title("Seno")
# ax1.set_xlabel('Eixo X')
# ax1.set_ylabel('Eixo Y')
# ax1.grid(True, linestyle="--", alpha=0.5)
# ax1.legend(["y = sin(x)"])
# ax2.plot(x, y2)
# ax2.set_title("Cosseno")
# ax2.set_xlabel('Eixo X')
# ax2.set_ylabel('Eixo Y')
# ax2.grid(True, linestyle="--", alpha=0.5)
# ax2.legend(["y = cos(x)"])
# plt.tight_layout()
# plt.show()

# 8️⃣ Use matplotlib.widgets.Slider para criar um gráfico interativo de y = sin(fx), onde f é controlado por um slider variando de 1 a 10.
# x = np.linspace(0, 2 * np.pi, 1000)
# f_inicial = 1
# y = np.sin(f_inicial * x)
# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.25)
# linha, = plt.plot(x, y, lw=2, color="blue", label=f"y = sin({f_inicial}x)")
# plt.title("Gráfico Interativo de y = sin(fx)")
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.legend()
# ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03]) 
# slider_f = Slider(ax_slider, "Frequência (f)", 1, 10, valinit=f_inicial, valstep=0.1)
# def update(val):
#     f = slider_f.val 
#     linha.set_ydata(np.sin(f * x))  
#     linha.set_label(f"y = sin({f:.1f}x)")  # Atualiza a legenda
#     plt.legend()
#     fig.canvas.draw_idle()
# slider_f.on_changed(update)
# plt.show()
