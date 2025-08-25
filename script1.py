pip install scikit-learn


from sklearn.datasets import load_iris
import pandas as pd

# Cargar dataset Iris
iris = load_iris()

# Convertir a DataFrame para explorarlo
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target  # especie como número
df["species"] = df["target"].apply(lambda i: iris.target_names[i])  # especie como texto

print(df.head())


X = iris.data         # variables independientes (medidas de la flor)
y = iris.target       # variable dependiente (especie: 0, 1, 2)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

from sklearn.neighbors import KNeighborsClassifier

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = modelo.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

import numpy as np

# Medidas de una flor: [longitud_sepalo, ancho_sepalo, longitud_petalo, ancho_petalo]
flor = np.array([[5.1, 3.5, 1.4, 0.2]])
prediccion = modelo.predict(flor)

print("Predicción:", iris.target_names[prediccion[0]])