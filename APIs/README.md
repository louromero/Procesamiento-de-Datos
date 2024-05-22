# Procesando información en bruto

## Introducción

En esta parte del proyecto, imaginemos que no tenemos acceso fácil a estos datos a través de la librería `datasets` y, en su lugar, necesitamos descargar los datos manualmente usando `requests`.

## Tarea

Realizaremos un GET request para descargar los datos y escribir la respuesta como un archivo de texto plano con extensión CSV. No utilizaremos pandas para esto, solo manipulación de archivos nativa de Python.

### Instrucciones

1. **Descargar los Datos**: Realizar un GET request a la URL proporcionada para obtener los datos en formato CSV.
2. **Escribir los Datos en un Archivo**: Guardar los datos descargados en un archivo de texto plano con extensión `.csv`.

`Los datos son accesibles en [esta dirección](https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv)`