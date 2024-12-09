import numpy as np
# One-Hot Encoding of Nominal Values

# Write a Python function to perform one-hot encoding of nominal values. The function should take in a 1D numpy array x of integer values and an optional
# integer n_col representing the number of columns for the one-hot encoded array. If n_col is not provided, it should be automatically determined from the input array.

# Example:
#     x = np.array([0, 1, 2, 1, 0])
#     output = to_categorical(x)
#     print(output)
#     # Output:
#     # [[1. 0. 0.]
#     #  [0. 1. 0.]
#     #  [0. 0. 1.]
#     #  [0. 1. 0.]
#     #  [1. 0. 0.]]
    
#     Reasoning:
#     Each element in the input array is transformed into a one-hot encoded vector,
#     where the index corresponding to the value in the input array is set to 1, 
#     and all other indices are set to 0.


def to_categorical(x, n_col=None):
    opa = []
    for i in x:
        semi_opa = []
        for j in range(np.max(x)+1): 
            if j == i:
                semi_opa.append(1)
            else:
                semi_opa.append(0)
        opa.append(semi_opa)
        
    return opa

# solucao deles:
# def to_categorical(x, n_col=None):
#     # One-hot encoding of nominal values
#     # If n_col is not provided, determine the number of columns from the input array
#     if not n_col:
#         n_col = np.amax(x) + 1
#     # Initialize a matrix of zeros with shape (number of samples, n_col)
#     one_hot = np.zeros((x.shape[0], n_col))
#     # Set the appropriate elements to 1
#     one_hot[np.arange(x.shape[0]), x] = 1
#     return one_hot