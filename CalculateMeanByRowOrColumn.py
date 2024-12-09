
# Calculate Mean by Row or Column (easy)
# ✔
# Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode.
# The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

# Example1:
#         input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
#         output: [4.0, 5.0, 6.0]
#         reasoning: Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].
        
#         Example 2:
#         input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'row'
#         output: [2.0, 5.0, 8.0]
#         reasoning: Calculating the mean of each row results in [(1+2+3)/3, (4+5+6)/3, (7+8+9)/3].


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	sum = 0
	if mode == 'row':
		for i in matrix:
			for element in i:
				sum += element
			means.append(sum/len(matrix[0]))
			sum = 0
	else:
		for j in range(len(matrix)):
			for i in range(len(matrix)):
				sum += matrix[i][j]
				

# resoluçao deles:
# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
#     if mode == 'column':
#         return [sum(col) / len(matrix) for col in zip(*matrix)]
#     elif mode == 'row':
#         return [sum(row) / len(row) for row in matrix]
#     else:
#         raise ValueError("Mode must be 'row' or 'column'")