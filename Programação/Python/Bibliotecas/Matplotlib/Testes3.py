import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Cria os dados iniciais
x = np.linspace(0, 2 * np.pi, 1000)
frequencia_inicial = 1
y = np.sin(frequencia_inicial * x)

# Cria a figura e o gráfico
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Ajusta o layout para dar espaço ao slider
linha, = plt.plot(x, y, lw=2, color="blue")
plt.title("Gráfico de Seno com Slider")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True, linestyle="--", alpha=0.5)

# Cria o slider
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])  # Posição e tamanho do slider
slider = Slider(ax_slider, "Frequência", 1, 10, valinit=frequencia_inicial, valstep=0.5)

# Função para atualizar o gráfico quando o slider é movido
def update(val):
    frequencia = slider.val
    linha.set_ydata(np.sin(frequencia * x))  # Atualiza os dados do gráfico
    fig.canvas.draw_idle()  # Redesenha o gráfico

# Conecta o slider à função de atualização
slider.on_changed(update)

# Exibe a janela gráfica
plt.show()