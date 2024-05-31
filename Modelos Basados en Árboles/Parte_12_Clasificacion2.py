import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score

# Carga de datos
data = pd.read_csv('datos_limpios.csv')

# Eliminamos columnas: "DEATH_EVENT", "categoria_edad"
X = data.drop(columns=["DEATH_EVENT", "categoria_edad"])
y = data["DEATH_EVENT"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Calculamos la matriz de confusion
y_pred = rf.predict(X_test)
matriz_confusion = confusion_matrix(y_test, y_pred)
print("Matriz de confusión: ")
print(matriz_confusion)

# Calculamos el F1 Score
f1 = f1_score(y_test, y_pred)

# Comparamos con el acurry
accuracy = accuracy_score(y_test, y_pred)

print(f"F1 Score: {f1:.2f}")
print(f"Accuracy: {accuracy:.2f}")

# Obtenemos mejor resultado
best_f1 = 0
best_estimators = 1

for n in range(10, 200, 5):
    rf = RandomForestClassifier(n_estimators=n)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    if f1 > best_f1:
        best_f1 = f1
        best_estimators = n

print(f"Mejor F1-Score: {best_f1:.2f}")
print(f"Mejor estimators: {best_estimators}")
