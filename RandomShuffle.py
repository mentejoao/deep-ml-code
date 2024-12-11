import numpy as np


# Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them.
# The function should have an optional seed parameter for reproducibility.

# Example:
#     X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8]])
#     y = np.array([1, 2, 3, 4])
#     output: (array([[5, 6],
#                     [1, 2],
#                     [7, 8],
#                     [3, 4]]), 
#              array([3, 1, 4, 2]))

def shuffle_data(X, y, seed=None):
  
    np.random.seed(seed)
    combined = list(zip(X, y))
    np.random.shuffle(combined)
    X_shuffled, y_shuffled = zip(*combined) # unzip
    return list(X_shuffled), list(y_shuffled)

# resoluçao deles:
# def shuffle_data(X, y, seed=None):
#     if seed:
#         np.random.seed(seed)
#     idx = np.arange(X.shape[0])
#     np.random.shuffle(idx)
#     return X[idx], y[idx]