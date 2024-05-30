import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('Visualización/Integradores/datos_limpios.csv')

categories = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
titles = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

# Configuramos el subplots
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

# Graficos de Tortas
for i, category in enumerate(categories):
    counts = data[category].value_counts()
    axs[i].pie(
        counts,
        labels=['NO', 'SI'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff7777','#66b4b4']
    )
    axs[i].set_title(titles[i])

plt.show()
