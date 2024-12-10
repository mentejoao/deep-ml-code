import numpy as np
# Implement Recall Metric in Binary Classification
# Task: Implement Recall in Binary Classification
# Your task is to implement the recall metric in a binary classification setting.
# Recall is a performance measure that evaluates how effectively a machine learning model identifies positive instances from all the actual positive cases in a dataset.

# You need to write a function recall(y_true, y_pred) that calculates the recall metric. The function should accept two inputs

# Your function should return the recall value rounded to three decimal places. If the denominator (TP + FN) is zero, the recall should be 0.0 to avoid division by zero.

# Example:
# import numpy as np

# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])

# print(recall(y_true, y_pred))

# # Expected Output:
# # 0.75

def recall(y_true, y_pred):
	
    # tp / tp + fn

    tp = np.sum((y_true == 1) & (y_pred == 1))
    

    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    if tp + fn == 0:
        return 0.0
    
    return round(tp / (tp + fn), 4)


