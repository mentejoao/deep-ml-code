import numpy as np

# lembrando que essa igualdade é a chave
# para esta demonstração: z^t * z = sum(zi²)

# no final, ao partirmos da igualdade acima, derivando e igualando a zero, chegamos que
# theta = (X.T @ X)^-1 @ X.T @ y


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    
    if np.linalg.det(X.T @ X) != 0:
        theta = np.linalg.inv(X.T @ X) @ X.T @ y
    else:
        theta = np.linalg.pinv(X.T @ X) @ X.T @ y
    
    return np.round(theta, 4)