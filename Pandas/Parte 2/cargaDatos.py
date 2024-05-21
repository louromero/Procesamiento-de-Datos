import numpy as np
import pandas as pd
from datasets import load_dataset

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")

# Accedemos a todos los registos indexando por esa partición
data = dataset["train"]

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
perecieron = df[df["is_dead"]==1]
sobrevivieron = df[df["is_dead"]==0]

# Calcular los promedios de las edades de cada dataset e imprimir.
promedio_perecieron = perecieron["age"].mean()
promedio_sobrevivieron = sobrevivieron["age"].mean()

print(f"Edad promedio de las personas que perecieron: {promedio_perecieron:.2f} años")
print(f"Edad promedio de las personas que sobrevivieron: {promedio_sobrevivieron:.2f} años")