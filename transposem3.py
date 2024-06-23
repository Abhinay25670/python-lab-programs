def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate over the original matrix and fill in the transpose matrix
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Sample Input
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# Print the original matrix
print("Matrix before transposition:", matrix)

# Get the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transpose of the matrix
print("Matrix after transposition:", transposed_matrix)
