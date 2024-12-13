# Dice Score

# Your task is to implement a function dice_score(y_true, y_pred) that calculates the Dice Score, also known as the Sørensen–Dice coefficient or F1-score, for binary classification. The Dice Score is used to measure the similarity between two sets, particularly in tasks like image segmentation and binary classification.

# Return the Dice Score rounded to 3 decimal places, and handle edge cases appropriately (e.g., when there are no true or predicted positives).

# Example:
# y_true = np.array([1, 1, 0, 1, 0, 1])
# y_pred = np.array([1, 1, 0, 0, 0, 1])
# print(dice_score(y_true, y_pred))
# Output: 0.857

import numpy as np

# dice score = f1-score = Dice-Sørensen coefficient

# lembrando da formula
# dice score = 2*tp / (2*tp + fn + fp) ou 2|A U B| / (|A| + |B|)
# dice score = 2*Iou / (IoU + 1), onde IoU = tp / (fp + fn + tp)

def dice_score(y_true, y_pred):
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	if tp == 0:
		return 0.0
	
	res = 2*tp/(2*tp + fn + fp)
	
	return round(res, 3)
