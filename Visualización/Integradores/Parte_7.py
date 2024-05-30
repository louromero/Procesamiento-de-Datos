import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('Visualización/Integradores/datos_limpios.csv')

# Histograma
plt.figure(figsize=(10, 5))
plt.hist(data['age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], color='blue', edgecolor='black')
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad")
plt.show()

# Gráficos agrupados por hombre y mujer
labels = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

# Definir los datos de hombres
hombres = [
    data[data['sex'] == 1]['anaemia'].sum(),
    data[data['sex'] == 1]['diabetes'].sum(),
    data[data['sex'] == 1]['smoking'].sum(),
    data[data['sex'] == 1]['DEATH_EVENT'].sum()
]

# Definimos los datos de mujeres
mujeres = [
    data[data['sex'] == 0]['anaemia'].sum(),
    data[data['sex'] == 0]['diabetes'].sum(),
    data[data['sex'] == 0]['smoking'].sum(),
    data[data['sex'] == 0]['DEATH_EVENT'].sum()
]

x = range(len(labels))

plt.figure(figsize=(10, 5))
plt.bar(x, hombres, width=-0.4, label='Hombres', color='blue', align='edge')
plt.bar(x, mujeres, width=0.4, label='Mujeres', color='red', align='edge')
plt.xticks(x, labels)
plt.title("Histograma Agrupado por Sexo")
plt.xlabel("Categorías")
plt.ylabel("Cantidad")
plt.legend()
plt.show()
