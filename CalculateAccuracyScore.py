import numpy as np

# Calculate Accuracy Score (Easy)

# Write a Python function to calculate the accuracy score of a model's predictions.
# The function should take in two 1D numpy arrays: y_true, which contains the true labels, and y_pred, which contains the predicted labels.
# It should return the accuracy score as a float.

def accuracy_score(y_true, y_pred):
	total_miss = np.abs(y_true-y_pred)
	accuracy = 1 - (np.sum(total_miss) / len(y_true))
	return accuracy

# def accuracy_score(y_true, y_pred):
#     accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
#     return accuracy