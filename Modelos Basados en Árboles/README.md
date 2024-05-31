# Parte 11: Clasificación 1
Ahora vamos a empezar a usar el dataset para lo que fue creado, ajustar un modelo de clasificación.

1. Grafica la distribución de clases (con la librería de tu preferencia) para analizar si este dataset está balanceado o no
2. Realiza la partición del dataset en conjunto de entrenamiento y test
    - Esta partición debe ser estratificada
    - Para lograrlo debes usar el parámetro como stratify=y en la función train_test_split
3. Ajusta un árbol de decisión y calcula el accuracy sobre el conjunto de test.
4. Trata de mover los valores de los parámetros para lograr la mayor accuracy que puedas.

## Nota:
No olvides eliminar la colúmna `categoria_edad.`