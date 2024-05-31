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

# Parte 12: Clasificación 2
Sobre el dataset ya particionado en conjuntos de entrenamiento y test, realiza lo siguiente:

1. Ajusta un random forest
2. Calcula su matriz de confusión
3. Calcula F1-Score y compara con el accuracy
4. Trata de cambiar los valores de los parámetros del random forest para conseguir el mejor resultado que puedas.

## Nota:
No olvides eliminar la colúmna `categoria_edad`.