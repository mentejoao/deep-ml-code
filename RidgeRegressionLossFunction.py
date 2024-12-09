import numpy as np

# Implement Ridge Regression Loss Function
# Write a Python function `ridge_loss` that implements the Ridge Regression loss function.
#  The function should take a 2D numpy array `X` representing the feature matrix, a 1D numpy array `w` representing the coefficients,
#  a 1D numpy array `y_true` representing the true labels, and a float `alpha` representing the regularization parameter. The function should return the Ridge loss,
#  which combines the Mean Squared Error (MSE) and a regularization term.

# Example:
# import numpy as np

# X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
# w = np.array([0.2, 2])
# y_true = np.array([2, 3, 4, 5])
# alpha = 0.1

# loss = ridge_loss(X, w, y_true, alpha)
# print(loss)
# Expected Output: 2.204

## Explicação:
# A Regressão Linear Ridge é um método de regressão linear com regularização para prevenir overfitting
# É adicionado o termo da soma do quadrado dos coeficientes multiplicado por um parâmetro (que controla a força da regularização)
# A regularização adiciona uma penalidade para a loss function 

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	loss = np.sum((np.sum(X*w, axis=1)-y_true)**2)/X.shape[0] + alpha*np.sum(w**2)
	return loss


# def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
#     loss = np.mean((y_true - X @ w)**2) + alpha * np.sum(w**2)
#     return loss