
import math

# Single Neuron (easy)
# Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, handling multidimensional input features. The function should take a list of feature vectors (each vector representing multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and bias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between the predicted probabilities and the true labels, both rounded to four decimal places.
# Example
# Example:
#         input: features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
#         output: ([0.4626, 0.4134, 0.6682], 0.3349)
#         reasoning: For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight,
#         adding these up along with the bias, then applying the sigmoid function to produce a probability. The MSE is calculated as
#         the average squared difference between each predicted probability and the corresponding true label.


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for element in features:
        for x, w in zip(element, weights):
            sum += element*weights
        sum += bias
        sigmoid = 1/(1+math.exp(-sum))
        probabilities.append(sigmoid)

    for probs in probabilities:
        for x, label in zip(probs, labels):
            mse += (x - label)**2
    
    mse = mse / len(labels)
    mse = round(mse, 4) # já é um float da pra fazer round direto
    probabilities = [round(p, 4) for p in probabilities] # round nao pode ser usado em listas, por isso devemos iterar em cada elemento

    return probabilities, mse