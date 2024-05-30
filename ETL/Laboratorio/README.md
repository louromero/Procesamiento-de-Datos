# Análisis de Calidad del Aire

Este proyecto analiza los `datos demográficos` y de `calidad del aire` de ciudades en Estados Unidos. 
A continuación se describen los pasos para cargar, limpiar, procesar y analizar estos datos.

## Ejercicio 1: Cargar Datos Demográficos

Carga los datos demográficos en una tabla utilizando `pandas`, haciendo uso del mismo CSV de demografía del ejemplo estudiado en clases.

```python
import pandas as pd

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    return data
```

## Ejercicio 2: Cargar Datos de Calidad del Aire

Parsea los datos de calidad del aire para cada ciudad en la tabla demográfica obteniendo la información con la [API](https://api-ninjas.com/api/airquality).

```python
import requests
import pandas as pd
from typing import Set

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> pd.DataFrame:
    api_key = 'YOUR_API_KEY'  # No olvidar reemplazar con tu API key
    air_quality_data = []

    for city in ciudades:
        url = f"https://api.api-ninjas.com/v1/airquality?city={city}"
        response = requests.get(url, headers={'X-Api-Key': api_key})
        if response.status_code == 200:
            data = response.json()
            if data:
                data_entry = {
                    'city': city,
                    'CO': data['CO']['concentration'],
                    'NO2': data['NO2']['concentration'],
                    'O3': data['O3']['concentration'],
                    'SO2': data['SO2']['concentration'],
                    'PM2.5': data['PM2.5']['concentration'],
                    'PM10': data['PM10']['concentration'],
                    'overall_aqi': data['overall_aqi']
                }
                air_quality_data.append(data_entry)

    air_quality_df = pd.DataFrame(air_quality_data)
    air_quality_df.to_csv('ciudades.csv', index=False)
    return air_quality_df
```
Como se puede observar, nosotros obtenemos los datos de la calidad del aire para un conjunto de ciudades utilizando una API y devolviendo dichos datos en un DataFrame de pandas. Además, los datos son guardados un un archivo CSV por si es requerido en un futuro.

## Ejercicio 3: Limpieza de Datos Demográficos

Limpia los datos demográficos realizando las siguientes acciones:

- Elimina las columnas: Race, Count y Number of Veterans.
- Elimina las filas duplicadas.

```python
import pandas as pd

def limpiar_datos_demograficos(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminar columnas innecesarias
    df = df.drop(columns=['Race', 'Count', 'Number of Veterans'])
    
    # Eliminar filas duplicadas
    df = df.drop_duplicates()
    
    return df
```

## Ejercicio 4: Crear Base de Datos SQLite

Crea una base de datos en SQLite, carga las dos tablas procesadas ahí.

```python
import sqlite3

def crear_base_datos_sqlite(df_demograficos: pd.DataFrame, df_calidad_aire: pd.DataFrame) -> sqlite3.Connection:
    conn = sqlite3.connect('calidad_aire.db')
    
    df_demograficos.to_sql('demografia', conn, if_exists='replace', index=False)
    df_calidad_aire.to_sql('calidad_aire', conn, if_exists='replace', index=False)
    
    return conn
```

## Ejercicio 5: Análisis de Calidad del Aire

Aplica joins y agregaciones para verificar si las ciudades más pobladas tienen la peor calidad del aire.

```python
import pandas as pd

def analizar_calidad_aire(conn: sqlite3.Connection):
    query = """
    SELECT d.City, d."Total Population", a.overall_aqi 
    FROM demografia AS d
    JOIN calidad_aire AS a ON d.City = a.City
    ORDER BY d."Total Population" DESC
    LIMIT 10;
    """
    result = pd.read_sql(query, conn)
    return result
```

## Script Principal

Aquí está el script principal que ejecuta todos los pasos mencionados:

```python
if __name__ == "__main__":
    # Ejercicio 1
    df_demograficos = ej_1_cargar_datos_demograficos()
    print("Datos demográficos cargados.")

    # Ejercicio 2
    ciudades = set(df_demograficos['City'].tolist())
    df_calidad_aire = ej_2_cargar_calidad_aire(ciudades)
    print("Datos de calidad del aire cargados.")

    # Ejercicio 3
    df_demograficos = limpiar_datos_demograficos(df_demograficos)
    print("Datos demográficos limpiados.")

    # Ejercicio 4
    conn = crear_base_datos_sqlite(df_demograficos, df_calidad_aire)
    print("Base de datos SQLite creada y tablas cargadas.")

    # Ejercicio 5
    resultado_analisis = analizar_calidad_aire(conn)
    print("Resultado del análisis:")
    print(resultado_analisis)

    # Guardar resultados en un archivo CSV
    resultado_analisis.to_csv('resultado_analisis.csv', index=False)
    print("Resultado del análisis guardado en 'esultado_analisis.csv'")
```

