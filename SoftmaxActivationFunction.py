import math

# Write a Python function that computes the softmax activation for a given list of scores.
# The function should return the softmax values as a list, each rounded to four decimal places.

# Example: input: scores = [1, 2, 3]
#          output: [0.0900, 0.2447, 0.6652]
#          reasoning: The softmax function converts a list of values into a probability distribution.
# The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.

def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    sum_exp_scores = sum(exp_scores)
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores]
    
    return probabilities

   