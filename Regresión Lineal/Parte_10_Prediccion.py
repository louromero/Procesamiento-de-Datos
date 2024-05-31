import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos
data = pd.read_csv('Visualización/Integradores/datos_limpios.csv')

# Eliminamos las columnas "DEATH_EVENT", "age", "categoria_edad"
X = data.drop(columns=['DEATH_EVENT', 'age', "categoria_edad"])
y = data['age']
print(X.head())

# Ajustar regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecimos las edades
y_pred = model.predict(X)

# Calculamos el MSE
mse = mean_squared_error(y, y_pred)
print(f"Error Cuadrático Medio: {mse:.2f}")