# Program: Matrix Operations using Nested Lists
# Perform:
# (a) Display in tabular format
# (b) Matrix addition with another matrix
# (c) Matrix transpose
# (d) Sum of each row and column
# (e) Sum of main diagonal

matA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("--- Matrix A ---")
for row in matA:
    print(row)

# Addition
add_result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matA[i][j] + matB[i][j])
    add_result.append(row)

print("\n--- Matrix Addition (A + B) ---")
for r in add_result:
    print(r)

# Transpose of A
transpose = []
for j in range(3):
    row = []
    for i in range(3):
        row.append(matA[i][j])
    transpose.append(row)

print("\n--- Transpose of Matrix A ---")
for r in transpose:
    print(r)

# Row and Column sums
print("\n--- Row and Column Sums of Matrix A ---")
for i in range(3):
    print(f"Row {i + 1} Sum: {sum(matA[i])}")

for j in range(3):
    col_sum = sum(matA[i][j] for i in range(3))
    print(f"Column {j + 1} Sum: {col_sum}")

# Diagonal sum
diag_sum = sum(matA[i][i] for i in range(3))
print("Main Diagonal Sum:", diag_sum)
