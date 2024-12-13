from collections import Counter

# Task: Generate a Confusion Matrix
# Your task is to implement the function confusion_matrix(data) that generates a confusion matrix for a binary classification problem.
# The confusion matrix provides a summary of the prediction results on a classification problem, allowing you to visualize how many data points were correctly or incorrectly labeled.

# Input: A list of lists, where each inner list represents a pair [y_true, y_pred] for one observation.

# Output: A 2x2 confusion matrix.

def confusion_matrix(data):
	tp = 0
	fn = 0
	fp = 0
	tn = 0
	
	for pair in data:
		if pair[0] == pair[1] and pair[0] == 0:
			tn += 1
		elif pair[0] == pair[1] and pair[1] == 1:
			tp += 1
		elif pair[0] != pair[1] and pair[0] == 1:
			fn += 1
		elif pair[0] != pair[1] and pair[0] == 0:
			fp += 1
			
	matriz_confusao = [[tp, fn], [fp, tn]]
			
	return matriz_confusao

# resoluçao deles (utilizando count):
# def confusion_matrix(data):
#     # Count all occurrences
#     counts = Counter(tuple(pair) for pair in data)
#     # Get metrics
#     TP, FN, FP, TN = counts[(1, 1)], counts[(1, 0)], counts[(0, 1)], counts[(0, 0)]
#     # Define matrix and return
#     confusion_matrix = [[TP, FN], [FP, TN]]
#     return confusion_matrix
