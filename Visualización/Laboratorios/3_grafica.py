import plotly.graph_objects as go
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

# Filtramos los datos
matematicas = df[df["materia"] == "Matemáticas"]
historia = df[df["materia"] == "Historia"]
ciencias = df[df["materia"] == "Ciencias"]
lenguaje = df[df["materia"] == "Lenguaje"]

# Boxplot
fig = go.Figure()
fig.add_trace(go.Box(y=matematicas["nota"].values, name='Matemáticas'))
fig.add_trace(go.Box(y=historia["nota"].values, name='Historia'))
fig.add_trace(go.Box(y=ciencias["nota"].values, name='Ciencias'))
fig.add_trace(go.Box(y=lenguaje["nota"].values, name='Lenguaje'))

fig.update_layout(title='Gráfico de Cajas', yaxis_title='Valores')
fig.show()

# Grafico de torta
aprobados = df['aprobado'].value_counts()
labels = ['Aprobados', 'No Aprobados']

fig = go.Figure()
fig.add_trace(go.Pie(labels=labels, values=aprobados))
fig.update_layout(title='Gráfico de Torta')
fig.show()
