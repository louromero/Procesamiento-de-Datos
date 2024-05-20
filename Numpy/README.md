# Análisis de Datos sobre Fallo Cardíaco

## Introducción

El proyecto de este curso consiste en analizar el conjunto de datos introducido en esta sección, procesarlo, limpiarlo y finalmente ajustar modelos de machine learning para realizar predicciones sobre estos datos.

## Tarea

Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio.

## Requisitos Previos

Para comenzar, es necesario instalar la librería `datasets` de Huggingface. Esto se puede hacer ejecutando el siguiente comando en tu entorno de desarrollo:

```bash
pip install datasets
```

## Descripción del Dataset

El dataset contiene registros médicos de 299 pacientes que padecieron insuficiencia cardíaca durante un período de seguimiento. Las 13 características clínicas incluidas en el conjunto de datos son:

1. **Edad**: Edad del paciente (años)
2. **Anemia**: Disminución de glóbulos rojos o hemoglobina (booleano)
3. **Presión arterial alta**: Si el paciente tiene hipertensión (booleano)
4. **Creatinina fosfoquinasa (CPK)**: Nivel de la enzima CPK en la sangre (mcg/L)
5. **Diabetes**: Si el paciente tiene diabetes (booleano)
6. **Fracción de eyección**: Porcentaje de sangre que sale del corazón en cada contracción (porcentaje)
7. **Plaquetas**: Plaquetas en la sangre (kiloplaquetas/mL)
8. **Sexo**: Mujer u hombre (binario)
9. **Creatinina sérica**: Nivel de creatinina sérica en la sangre (mg/dL)
10. **Sodio sérico**: Nivel de sodio sérico en la sangre (mEq/L)
11. **Fumar**: Si el paciente fuma o no (booleano)
12. **Tiempo**: Período de seguimiento (días)
13. **[Objetivo] Evento de fallecimiento**: Si el paciente falleció durante el período de seguimiento (booleano)

## Descarga y Estructura del Dataset

Para descargar el dataset utilizando la librería `datasets`, ejecutamos el siguiente código:

```python
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
```

El dataset contiene una estructura similar a un diccionario con particiones de datos y características. Debido a que este dataset solo contiene una partición llamada `train`, accedemos a todos los registros indexando por esa partición:

```python
data = dataset["train"]
```

`data` es un objeto `Dataset` que permite indexar por sus atributos como un diccionario. Tiene la siguiente estructura:

```python
Dataset({
    features: [
        'age',
        'has_anaemia',
        'creatinine_phosphokinase_concentration_in_blood',
        'has_diabetes',
        'heart_ejection_fraction',
        'has_high_blood_pressure',
        'platelets_concentration_in_blood',
        'serum_creatinine_concentration_in_blood',
        'serum_sodium_concentration_in_blood',
        'is_male',
        'is_smoker',
        'days_in_study',
        'is_dead'
    ],
    num_rows: 299
})
```

Al indexar por una característica, obtenemos una lista con los valores de todos los registros para esa columna.
