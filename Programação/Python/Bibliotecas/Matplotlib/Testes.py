import matplotlib.pyplot as plt
import numpy as np

# Dados
categorias = ["A", "B", "C", "D"]
valores = [10, 20, 15, 25]

# Cria uma figura com 3 subplots (3 linhas, 1 coluna)
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(8, 12))

# Gráfico de barras verticais (ax1)
ax1.bar(categorias, valores, color="green", label="Valores")
ax1.set_title("Gráfico de Barras Verticais")  # Título do ax1
ax1.set_xlabel("Categorias")  # Rótulo do eixo x
ax1.set_ylabel("Valores")     # Rótulo do eixo y
ax1.legend()

# Gráfico de barras horizontais (ax2)
ax2.barh(categorias, valores, color="orange", label="Valores")
ax2.set_title("Gráfico de Barras Horizontais")  # Título do ax2
ax2.set_xlabel("Valores")  # Rótulo do eixo x
ax2.set_ylabel("Categorias")  # Rótulo do eixo y
ax2.legend()

# Gráfico de pizza (ax3)
ax3.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90, colors=["red", "blue", "green", "purple"])
ax3.set_title("Gráfico de Pizza")  # Título do ax3

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Exibe a figura
plt.show()