import numpy as np

# Task: Compute Root Mean Square Error (RMSE)
# In this task, you are required to implement a function rmse(y_true, y_pred) that calculates the Root Mean Square Error (RMSE) between the actual values and the predicted values.
# RMSE is a commonly used metric for evaluating the accuracy of regression models, providing insight into the standard deviation of residuals.

# Your Task: Implement the function rmse(y_true, y_pred) to return the RMSE value rounded to three decimal places.
# Ensure your function handles edge cases such as mismatched array shapes and empty arrays appropriately.

# Example:
# y_true = np.array([3, -0.5, 2, 7])
# y_pred = np.array([2.5, 0.0, 2, 8])
# print(rmse(y_true, y_pred))
# Output: 0.612

def rmse(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")
    
    if y_true.size == 0: 
        raise ValueError("Arrays cannot be empty")
    
    error_sum = np.sum((y_true - y_pred) ** 2)
    
    rmse_res = np.sqrt(error_sum / y_true.size)
    return np.round(rmse_res, 3)

# import numpy as np

# def rmse(y_true, y_pred):
#     if y_true.shape != y_pred.shape:
#         raise ValueError("Arrays must have the same shape")
#     if y_true.size == 0:
#         raise ValueError("Arrays cannot be empty")
#     return round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)