import numpy as np
from datasets import load_dataset

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")

# Accedemos a todos los registos indexando por esa partición
data = dataset["train"]

# Obtenemos las edades (lista)
edades = data['age']

# Convertimos la lista en un arreglo
array = np.array(edades)

# Calculamos promecio
promedio_edad = np.mean(array)

# Mostramos resultado
print(f"Edad promedio de las personas participantes en el estudio: {promedio_edad:.2f} años")