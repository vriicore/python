# Program: Matrix Transpose Using Lambda
# Take a matrix as input and transpose its elements using lambda.
# Eg. matrix = [[1, 2], [3, 4], [5, 6], [7, 8]] -> [[1, 3, 5, 7], [2, 4, 6, 8]]

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

transpose_lambda = lambda mat: [list(row) for row in zip(*mat)]
transposed = transpose_lambda(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
