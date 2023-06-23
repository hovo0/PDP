def multiply_matrices(A, B):
    """
    Multiply two matrices A and B.
    :param A: Matrix A
    :param B: Matrix B
    :return: The resulting matrix after multiplication.
    """
    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Get matrix A from input
A = []
print("Enter elements for matrix A (3x3):")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input("Enter element A[{}][{}]: ".format(i, j)))
        row.append(element)
    A.append(row)

# Get matrix B from input
B = []
print("Enter elements for matrix B (3x4):")
for i in range(3):
    row = []
    for j in range(4):
        element = int(input("Enter element B[{}][{}]: ".format(i, j)))
        row.append(element)
    B.append(row)

# Multiply the matrices
result = multiply_matrices(A, B)

# Print the result
print("Resultant matrix:")
for r in result:
    print(r)
