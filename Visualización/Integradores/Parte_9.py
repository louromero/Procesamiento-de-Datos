import pandas as pd
from sklearn.manifold import TSNE
import plotly.graph_objects as go

# Cargar los datos
data = pd.read_csv('Visualización/Integradores/datos_limpios.csv')

# Eliminamos las columnas DEATH_EVENT y categoria_edad
X = data.drop(columns=['DEATH_EVENT', "categoria_edad"]).values

# Exportamos array
y = data['DEATH_EVENT'].values

# Ejecutar el siguiente fragmento de código
X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

# Gráfico de dispersión
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=X_embedded[:, 0],
            y=X_embedded[:, 1],
            z=X_embedded[:, 2],
            mode='markers',
            marker=dict(
                size=6,
                color=y,
                colorscale=[[0, 'blue'], [1, 'red']],
                opacity=0.8
            )
        )
    ]
)

fig.update_layout(title='TSNE de Pacientes')
fig.show()
