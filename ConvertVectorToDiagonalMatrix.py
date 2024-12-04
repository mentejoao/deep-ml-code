import numpy as np

# Convert Vector to Diagonal Matrix (Easy)
# Write a Python function to convert a 1D numpy array into a diagonal matrix. The function should take in a 1D numpy array x and return a 2D numpy array representing the diagonal matrix.
# Example
# Example:
#     x = np.array([1, 2, 3])
#     output = make_diagonal(x)
#     print(output)
#     # Output:
#     # [[1. 0. 0.]
#     #  [0. 2. 0.]
#     #  [0. 0. 3.]]
    
#     Reasoning:
#     The input vector [1, 2, 3] is converted into a diagonal matrix where the elements of the vector form the diagonal of the matrix.


## converter um vetor em uma matriz diagonal
# lembrando que matriz diagonal é aquela em que só existe elementos em colunas, onde i=j, o resto é 0;

def make_diagonal(x):
	size = len(x)
	y = np.zeros((size, size))
	for i in range(size):
		for j in range(size):
			if i == j:
				y[i][j] = x[i]
			else:
				y[i][j] = 0
	return y

# soluções mais elegantes:

# def make_diagonal(x):
#     identity_matrix = np.identity(np.size(x))
#     return (identity_matrix*x)

# def make_diagonal(x):
#   return np.diag(x)