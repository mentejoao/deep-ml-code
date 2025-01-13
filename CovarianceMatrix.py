# lembrando a definicao da matriz de covariancia:
# cov(X,y) = sum 0 ... i (xi-xmedio)*(yi-ymedio) / n-1


## Calculate Covariance Matrix

# Write a Python function to calculate the covariance matrix for a given set of vectors.
# The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix
#  as a list of lists. Additionally, provide test cases to verify the correctness of your implementation.

# input: [[1, 2, 3], [4, 5, 6]], x: 1, 2, 3; -> portanto, xmedio: 6/3 = 2 // y: 4, 5, 6; -> portanto, ymedio: 15/3 = 5
# output: [[1.0, 1.0], [1.0, 1.0]] 
# matriz de cov: cov(X,X) cov(X, Y)      ->     ((1-2)*(1-2) + (2-2)*(2-2) + (3-2)*(3-2) / 2)) ...
#                cov(Y, X) cov(Y , Y)

# The covariance between the two features is calculated based on their deviations from the mean.
# For the given vectors, both covariances are 1.0, resulting in a symmetric covariance matrix.



def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features = len(vectors)
    num_samples = len(vectors[0])
    
    mean = [sum(feature) / num_samples for feature in vectors]

    centralized_vectors = [[value - mean[i] for value in feature] for i, feature in enumerate(vectors)]

    covariance_matrix = [
        [
            sum(centralized_vectors[i][k] * centralized_vectors[j][k] for k in range(num_samples)) / (num_samples - 1)
            for j in range(num_features)
        ]
        for i in range(num_features)
    ]

    return covariance_matrix