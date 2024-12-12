import numpy as np
# Linear Regression Using Gradient Descent (easy)

# Write a Python function that performs linear regression using gradient descent. The function should
# take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations,
# and return the coefficients of the linear regression model as a NumPy array.
# Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

# Example:
# input: X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000
#         output: np.array([0.1107, 0.9513])
#         reasoning: The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

	m, n = X.shape
	theta = np.zeros((n, 1))

	for i in range(iterations):

		gradient = (X.T @ (X @ theta - y.reshape(-1, 1)))*(1/m) 
		theta -= alpha * gradient
		
	return np.round(theta.flatten(), 4)