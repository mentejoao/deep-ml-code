import numpy as np

# Linear Kernel Function

# Description:
# Write a Python function kernel_function that computes the linear kernel between two input vectors x1 and x2.
# The linear kernel is defined as the dot product (inner product) of two vectors.

def kernel_function(x1, x2):

	if x1.shape != x2.shape:
		raise ValueError("Vectors must have the same shape1")

	linear_kernel = sum([element1*element2 for element1, element2 in zip(x1, x2)])
	return linear_kernel


# def kernel_function(x1, x2):
#     return np.inner(x1, x2)

## um importante tópico desta solução é que a solução proposta utilizamos np.inner ao inves de np.dot
## e tambem ao inves de fazer esta soma da list comprehension (na vdd, a lista )
## para comportamentos de vetores 1D np.dot e np.inner fazem a mesma coisa: o produto escalar, isto é:
# x1 = np.array([1, 2, 3])
# x2 = np.array([4, 5, 6])
# x1 . x2 = 1*4 + 2*5 + 3*6 = 32
# np.inner(x1, x2) = np.dot(x1, x2)
# para vetores 2D ou que possuem dimensão maior que 1, elas possuem comportamentos diferentes
# a np.dot fará a multiplicação das matrizes, isto é:
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(np.dot(A, B))  
# Saída:
# [[19 22]
#  [43 50]]

# enquanto a np.inner fará o produto interno de seus vetores correspondentes
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(np.inner(A, B))
# Saída:
# [[17 23]   = 1*5 + 2*6 = 17 (pega a primeira linha de A com a primeira linha de B)
#  [39 53]]  = 1*7 + 2*8 = 23 (pega a primeira linha de A com a segunda linha de B)

