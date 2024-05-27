import pandas as pd

# Crear DataFrame
df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

def limpiar_y_preparar_datos(df):
    # Verificar valores faltantes
    valores_faltantes = df.isnull().sum().sum()
    if valores_faltantes > 0:  
        print(f"Valores faltantes por columna: {valores_faltantes}")
        # Eliminar filas con valores faltantes (si es necesario)
        # df = df.dropna()
    else:
        print("No se encontraron valores faltantes")

    # Eliminar filas repetidas
    valores_duplicados = df.duplicated().sum()
    if valores_duplicados > 0:
        df.drop_duplicates(inplace=True)
        print(f"Se eliminaron las {valores_duplicados} filas duplicadas")
    else:
        print("No se encontraron valores duplicados")

    # Identificar y eliminar valores atipicos
    for column in df.select_dtypes(include=['number']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))
        if outliers.any():
            df = df[~outliers]
    print(f'Se eliminaron valores atípicos')

    # Categorizar por edades
    bins = [0, 13, 20, 40, 60, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    print("Se categorizaron por edades")

    # Guardamos resultados
    df.to_csv('datos_limpios.csv', index=False)
    print("Se guardaron los resultados")

# Llamar a la función con el DataFrame
limpiar_y_preparar_datos(df)
