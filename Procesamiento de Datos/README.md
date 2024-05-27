# Limpieza y Preparación de Datos

## Introducción

En esta sección del proyecto, después de haber cargado el archivo CSV mediante el request anterior (APIs), realizaremos las siguientes tareas de limpieza y preparación de datos:

### Tareas

1. **Verificar Valores Faltantes**: Asegurarnos de que no existan valores faltantes en el DataFrame.
2. **Eliminar Filas Repetidas**: Verificar y eliminar cualquier fila duplicada en el DataFrame.
3. **Identificar y Eliminar Valores Atípicos**: Verificar si existen valores atípicos en el DataFrame y eliminarlos.
4. **Categorizar por Edades**: Crear una nueva columna que categorice a los individuos por rangos de edad:
    - 0-12: Niño
    - 13-19: Adolescente
    - 20-39: Joven adulto
    - 40-59: Adulto
    - 60-...: Adulto mayor
5. **Guardar el Resultado**: Guardar el DataFrame resultante en un archivo CSV.
