# Scalar Multiplication of a Matrix (easy)
# Write a Python function that multiplies a matrix by a scalar and returns the result.

# Example:
#         input: matrix = [[1, 2], [3, 4]], scalar = 2
#         output: [[2, 4], [6, 8]]
#         reasoning: Each element of the matrix is multiplied by the scalar

def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result