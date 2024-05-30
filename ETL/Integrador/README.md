# Automatización del Procesamiento de Datos

Este proyecto consiste en la creación de un script en Python que automatiza el proceso de descarga, conversión, categorización y exportación de datos para su análisis. 

El script se encarga de:

1. Descargar los datos desde una URL proporcionada.
2. Convertir los datos descargados a un DataFrame de pandas.
3. Categorizar los datos en grupos según ciertas condiciones.
4. Exportar el DataFrame resultante a un archivo CSV listo para su análisis.

## Uso

Para ejecutar el script, se hará uso del siguiente comando en la terminal:

```bash
python Parte_6_Automatizacion.py <URL>
```

Donde `<URL>` es la dirección desde donde se descargarán los datos en formato CSV.

## Ejemplo

```bash
python Parte_6_Automatizacion.py https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv
```

## Requisitos

- Librerías: `pandas`, `requests`

Puedes instalar las librerías necesarias utilizando pip:

```bash
pip install pandas requests
```

## Notas

- La URL debe apuntar a un archivo CSV con el formato esperado para que el script funcione correctamente.