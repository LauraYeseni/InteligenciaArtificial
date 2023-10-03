import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Cargar el conjunto de datos de enfermedad cardiaca
df = pd.read_csv("heart.csv")  # Asegúrate de reemplazar "tu_archivo.csv" con el nombre de tu archivo CSV

# Seleccionar características y etiquetas
# Para este ejemplo, seleccionaremos algunas columnas como características
# y la columna 'output' como etiquetas
X = df[
    [
        "age",
        "sex",
        "cp",
        "trtbps",
        "chol",
        "fbs",
        "restecg",
        "thalachh",
        "exng",
        "oldpeak",
        "slp",
        "caa",
        "thall",
    ]
].values
y = df["output"].values


# Definición de la clase Perceptron
class Perceptron(object):
    """Perceptron classifier.

    Parameters
    ------------
    eta : float
      Learning rate (between 0.0 and 1.0)
    n_iter : int
      Passes over the training dataset.
    random_state : int
      Random number generator seed for random weight
      initialization.

    Attributes
    -----------
    w_ : 1d-array
      Weights after fitting.
    errors_ : list
      Number of misclassifications (updates) in each epoch.

    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
          Training vectors, where n_examples is the number of examples and
          n_features is the number of features.
        y : array-like, shape = [n_examples]
          Target values.

        Returns
        -------
        self : object

        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


# Entrenar el perceptrón:
ppn = Perceptron(eta=0.1, n_iter=7)
ppn.fit(X, y)

# Graficar el número de actualizaciones de clasificación errónea
# en función de los Epochs
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker="o")
plt.xlabel("Epochs")
plt.ylabel("Numero de errores")
plt.show()
