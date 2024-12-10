import numpy as np
# Task: Implement F-Score Calculation for Binary Classification
# Your task is to implement a function that calculates the F-Score for a binary classification task.
#  The F-Score combines both Precision and Recall into a single metric, providing a balanced measure of a model's performance.

# Write a function f_score(y_true, y_pred, beta) where:

# y_true: A numpy array of true labels (binary).
# y_pred: A numpy array of predicted labels (binary).
# beta: A float value that adjusts the importance of Precision and Recall. When beta=1, it computes the F1-Score, a balanced measure of both Precision and Recall.
# The function should return the F-Score rounded to three decimal places.

# Example:
# import numpy as np

# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])
# beta = 1

# print(f_score(y_true, y_pred, beta))

# # Expected Output:
# # 0.857


def f_score(y_true, y_pred, beta):

    tp = np.sum((y_true == 1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    if tp + fn != 0:
        recall = tp / (tp + fn)
    else:
        recall = 0

    if fp + tp != 0:
        precision = tp / (fp + tp)
    else:
        precision = 0

    # quando adicionamos β damos pesos diferentes para a precision e recall
    # f1-score é um f-score (ou fβ-score) com β=1 (fun fact, nao sabia)
        
    # β < 1: mais peso a precision
    # um jeito fácil de pensar nisso é imaginar que β = 0, se β = 0, temos:
    # f-score = (1 + 0²)*precision*recall / (0*precision) + recall => assumindo recall != 0, temos: f-score = precision

    # β > 1: mais peso a recall
    # analogamente, se fizessemos β tendendo ao infinito, teriamos:
    # (precision*β²) + recall ~ precision*β²
    # e no numerador: (1+β²) ~ β²
    # logo na formula do f-score, teriamos: f-score = precision*recall*β²/precision*β²
    # portanto f-score = recall

    f_score = recall*precision*(1+beta**2)/(recall + precision*beta**2)

    return round(f_score, 3)