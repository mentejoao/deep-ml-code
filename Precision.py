import numpy as np
# Write a Python function `precision` that calculates the precision metric given two numpy arrays: `y_true` and `y_pred`.
# The `y_true` array contains the true binary labels, and the `y_pred` array contains the predicted binary labels.
# Precision is defined as the ratio of true positives to the sum of true positives and false positives.

# Example:
# import numpy as np

# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])

# result = precision(y_true, y_pred)
# print(result)
# # Expected Output: 1.0


def precision(y_true, y_pred):

	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))

	if tp + fp == 0:
		return 0.0
	
	precision_value = tp / (tp + fp)

	return precision_value
