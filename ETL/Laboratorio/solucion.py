import pandas as pd
import requests
from io import StringIO
import sqlite3
from typing import Set

# Ejercicio 1: Cargar datos demográficos
def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    response = requests.get(url, verify=False)
    data = pd.read_csv(StringIO(response.text), sep=';')
    return data

# Ejercicio 2: Cargar datos de calidad del aire
def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> pd.DataFrame:
    api_key = 'j60Nm4kEe89bc/wwD6IVJw==0zPvkuSpDVlYSh4q'
    air_quality_data = []

    for city in ciudades:
        url = f"https://api.api-ninjas.com/v1/airquality?city={city}"
        response = requests.get(url, headers={'X-Api-Key': api_key})
        
        # Solicitud API
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

    # Convertimos a un DataFrame
    air_quality_df = pd.DataFrame(air_quality_data)
    
    # Guardamos archivo en un CSV
    air_quality_df.to_csv('ciudades.csv', index=False)
    return air_quality_df

# Ejercicio 3: Limpieza de datos demográficos
def limpiar_datos_demograficos(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminamos columnas innecesarias
    df = df.drop(columns=['Race', 'Count', 'Number of Veterans'])
    
    # Eliminamos filas duplicadas
    df = df.drop_duplicates()
    
    return df

# Ejercicio 4: Crear base de datos SQLite y cargar tablas
def crear_base_datos_sqlite(df_demograficos: pd.DataFrame, df_calidad_aire: pd.DataFrame) -> sqlite3.Connection:
    
    # Creamos la base de datos
    conn = sqlite3.connect('calidad_aire.db')
    
    #Cargamos los datos
    df_demograficos.to_sql('demografia', conn, if_exists='replace', index=False)
    df_calidad_aire.to_sql('calidad_aire', conn, if_exists='replace', index=False)
    
    
    return conn

# Ejercicio 5: Aplicar joins y agregaciones para verificar la relación entre población y calidad del aire
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

# Script principal
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
