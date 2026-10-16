# Practical Exam Task 20:
# Create a matrix using nested lists and perform:
# - Matrix addition
# - Matrix transpose
# - Sum of each row
# - Sum of each column

# Matrix A (3x3)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B (3x3)
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("--- Matrix A ---")
for r in A:
    print(r)

print("\n--- Matrix B ---")
for r in B:
    print(r)

# 1. Matrix Addition
add_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    add_matrix.append(row)

print("\n1. Matrix Addition (A + B):")
for r in add_matrix:
    print(r)

# 2. Matrix Transpose (A)
transpose_A = []
for j in range(3):
    row = []
    for i in range(3):
        row.append(A[i][j])
    transpose_A.append(row)

print("\n2. Matrix Transpose of A:")
for r in transpose_A:
    print(r)

# 3. Sum of each row (A)
print("\n3. Sum of Each Row of A:")
for i in range(3):
    print(f"Row {i + 1} Sum = {sum(A[i])}")

# 4. Sum of each column (A)
print("\n4. Sum of Each Column of A:")
for j in range(3):
    col_sum = sum(A[i][j] for i in range(3))
    print(f"Column {j + 1} Sum = {col_sum}")
