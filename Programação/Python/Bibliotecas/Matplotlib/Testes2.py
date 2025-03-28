import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Cria o gráfico
plt.plot(x, y, color="green", marker="o", linestyle=":", label="y = sin(x)")

# Customizações
plt.title("Gráfico de Seno Customizado", fontsize=16, color="blue")
plt.xlabel("Eixo X", fontsize=12, color="red")
plt.ylabel("Eixo Y", fontsize=12, color="red")
plt.xlim(0, 10)  # Limites do eixo x
plt.ylim(-1.5, 1.5)  # Limites do eixo y
plt.grid(True, linestyle="--", color="gray", alpha=0.5)  # Grade
plt.legend(loc="upper right", fontsize=10)  # Legenda

# Adiciona texto
plt.text(
    5, 0, "Função Seno",  # Posição do texto
    fontsize=14, color="purple", ha="center", va="center",  # Estilo do texto
    bbox=dict(facecolor="yellow", alpha=0.5)  # Caixa de fundo
)

# Adiciona anotação para o máximo
plt.annotate(
    "Máximo",  # Texto da anotação
    xy=(np.pi/2, 1),  # Ponto a ser anotado
    xytext=(3, 1.2),  # Posição do texto
    arrowprops=dict(facecolor="red"),  # Seta vermelha
    fontsize=12, color="red"
)

# Adiciona anotação para o mínimo
plt.annotate(
    "Mínimo",  # Texto da anotação
    xy=(3*np.pi/2, -1),  # Ponto a ser anotado
    xytext=(8, -1.2),  # Posição do texto
    arrowprops=dict(facecolor="blue", shrink=0.05),  # Seta azul
    fontsize=12, color="blue"
)

# Exibe o gráfico
plt.show()