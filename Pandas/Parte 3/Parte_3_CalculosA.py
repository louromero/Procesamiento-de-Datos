import pandas as pd
from datasets import load_dataset

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")

# Accedemos a todos los registos indexando por esa partición
data = dataset["train"]

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificación de los tipos de datos
df.info()

# Calcular fumadores usando agregación
fumadores = df.groupby("is_male")["is_smoker"].sum()
print(fumadores)

mujeres = fumadores[0]
hombres = fumadores[1]

print(f"Mujeres fumadoras: {mujeres}")
print(f"Hombres fumadores: {hombres}")