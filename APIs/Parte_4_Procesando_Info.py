import requests

def descargar_datos(url):

    respuesta = requests.get(url)
    
    # Verificar el requests
    if respuesta.status_code == 200:
        # Nombre del archivo
        nombre_archivo = url.split('/')[-1]
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(respuesta.text)
        print(f'Los datos fueron guardados exitosamente!')    
    else:
        print(f'Error: No se pudo descargar los datos.')

# URL con los datos
url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
descargar_datos(url)
