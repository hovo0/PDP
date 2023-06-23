"""
This module provides a matrix multiplication function.
"""


def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply two matrices A and B.

    :param matrix_a: Matrix A.
    :param matrix_b: Matrix B.
    :return: The resulting matrix after multiplication.
    """
    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i, row_a in enumerate(matrix_a):
        for j, column_b in enumerate(zip(*matrix_b)):
            result[i][j] = sum(row_a[k] * column_b[k] for k in range(len(matrix_b)))

    return result


# Get matrix A from input
matrix_a_input = []
print("Enter elements for matrix A (3x3):")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element A[{i}][{j}]: "))
        row.append(element)
    matrix_a_input.append(row)

# Get matrix B from input
matrix_b_input = []
print("Enter elements for matrix B (3x4):")
for i in range(3):
    row = []
    for j in range(4):
        element = int(input(f"Enter element B[{i}][{j}]: "))
        row.append(element)
    matrix_b_input.append(row)

# Multiply the matrices
result = multiply_matrices(matrix_a_input, matrix_b_input)

# Print the result
print("Resultant matrix:")
for row in result:
    print(row)
