import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carga de datos
data = pd.read_csv('datos_limpios.csv')

# Gráfico de barras - DEATH_EVENT
death_event_counts = data["DEATH_EVENT"].value_counts()
death_event_counts.plot(kind='bar', color=['blue', 'red'])
plt.title("DISTRIBUCION DE CLASES")
plt.xlabel("Clase")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.show()

# Eliminamos columnas: "DEATH_EVENT", "categoria_edad"
X = data.drop(columns=["DEATH_EVENT", "categoria_edad"])
y = data["DEATH_EVENT"]

# Realizamos particion
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Ajustamos el árbol de decición
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Calculamos el acurracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

# Calculamos mejor acurracy
best_accuracy = 0
best_depth = 1

for depth in range(1, 20):
    clf = DecisionTreeClassifier(max_depth=depth)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_depth = depth

print(f"Acurracy mejor: {best_accuracy*100:.2f}% ")
print(f"Maxima profundidad: {best_depth}")