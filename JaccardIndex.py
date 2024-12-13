import numpy as np

# Task: Implement the Jaccard Index
# Your task is to implement a function jaccard_index(y_true, y_pred) that calculates the Jaccard Index, a measure of similarity between two binary sets.
# The Jaccard Index is widely used in binary classification tasks to evaluate the overlap between predicted and true labels.

# The function should handle cases where there is no overlap or when both arrays contain only zeros.

def jaccard_index(y_true, y_pred):
	
    ## jaccard index tbm é conhecido como IoU = |A intersect B| / |A U B|

    tp = np.sum((y_pred == 1) & (y_true == 1))
    fn = np.sum((y_pred == 1) & (y_true == 0))
    fp = np.sum((y_pred == 0) & (y_true == 1))
    result = tp / (tp + fn + fp)
    
    return round(result, 3)

# resolução deles:
# def jaccard_index(y_true, y_pred):
#     intersection = np.sum((y_true == 1) & (y_pred == 1))
#     union = np.sum((y_true == 1) | (y_pred == 1))
#     result = intersection / union
#     if np.isnan(result):
#         return 0.0
#     return round(result, 3)