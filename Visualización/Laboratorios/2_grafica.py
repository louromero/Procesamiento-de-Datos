import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas',
                'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia',
                'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias',
                'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Filtramos información
matematicas = df[df["materia"] == "Matemáticas"]
historia = df[df["materia"] == "Historia"]
ciencias = df[df["materia"] == "Ciencias"]
lenguaje = df[df["materia"] == "Lenguaje"]

# Establecemos el estilo adecuado para que se vean las cuadrillas como en el ejemplo dado
plt.style.use('fivethirtyeight')

# Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(
    [matematicas['nota'], historia['nota'], ciencias['nota'], lenguaje['nota']],
    labels=["Matemáticas", "Historia", "Ciencias", "Lenguaje"]
)
plt.title('Distribución de Notas')
plt.ylabel('Nota')
plt.show()

# Grafico de torta
aprobados = df['aprobado'].value_counts()
labels = ['Aprobados', 'No Aprobados']
plt.figure(figsize=(6, 6))
plt.pie(aprobados, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Aprobados')
plt.show()
