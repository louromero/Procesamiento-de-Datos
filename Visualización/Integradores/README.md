# Parte 7: Analizando distribuciones 1

Una vez tenemos los datos exportados por nuestro script de [ETL](https://github.com/louromero/Procesamiento-de-Datos/tree/master/ETL/Integrador), podemos proceder a realizar gráficas de análisis. 
En esta etapa del proyecto usamos matplotlib para:

1. Graficar la distribución de edades con un histograma
2. Graficar histogramas agrupado por hombre y mujer:
    - cantidad de anémicos
    - cantidad de diabéticos
    - cantidad de fumadores
    - cantidad de muertos

# Parte 8: Analizando distribuciones 2
Realizar una gráfica usando subplots, que contenga gráficas de torta que represente las distribuciones de:

- Cantidad de anémicos
- Cantidad de diabéticos
- Cantidad de fumadores
- Cantidad de muertos

# Parte 9: Analizando distribuciones 3
Para esta sección usaremos una [técnica de reducción de dimensionalidad](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding#:~:text=t-distributed%20stochastic%20neighbor%20embedding%20(t-SNE)%20is,two%20or%20three-dimensional%20map.) para tratar de visualizar aproximadamente la estructura de nuestros datos.

Los pasos a seguir para lograrlo son (partiendo del DataFrame anterior):

1. Exportar la una matriz con sólo los valores de los atributos en formato de numpy array
    - Para esto deberás usar df.drop(columns[<columna-objetivo>]) para eliminar la colúmna que contiene la información si la persona murió o no, también elimina categoria_edad.
    - Puedes convertir un dataframe a un numpy array con su atributo df.values.
2. Exportar un array unidimensional y de sólo la colúmna objetivo DEATH_EVENT.
Ejecutar el siguiente fragmento de código
```python
X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)
```
dónde `X_embedded` es un NumPy array de (299, 3)
3. Realizar un gráfico de dispersión 3D con Plotly donde los puntos de cada clase (vivo o muerto) tienen un color asignado para así poder diferenciarlos. (Para esto debes usar el vector y)

## Requisitos

- Librería: `pandas`, `matplotlib` , `scikit-learn`

Puedes instalar las librerías necesarias utilizando pip:

```bash
pip install pandas matplotlib scikit-learn
```