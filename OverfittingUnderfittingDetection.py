
# Write a Python function to determine whether a machine learning model is overfitting, underfitting,
# or performing well based on training and test accuracy values. The function should take two inputs:
# training_accuracy and test_accuracy. It should return one of three values: 1 if Overfitting, -1 if Underfitting,
# or 0 if a Good fit. The rules for determination are as follows:

# Overfitting: The training accuracy is significantly higher than the test accuracy (difference > 0.2).
# Underfitting: Both training and test accuracy are below 0.7.
# Good fit: Neither of the above conditions is true.

def model_fit_quality(training_accuracy, test_accuracy):
	"""
	Determine if the model is overfitting, underfitting, or a good fit based on training and test accuracy.
	:param training_accuracy: float, training accuracy of the model (0 <= training_accuracy <= 1)
	:param test_accuracy: float, test accuracy of the model (0 <= test_accuracy <= 1)
	:return: int, one of '1', '-1', or '0'.
	"""
	if training_accuracy - test_accuracy > 0.2:
		return 1
	elif training_accuracy < 0.7 and test_accuracy < 0.7:
		return -1
	else:
		return 0