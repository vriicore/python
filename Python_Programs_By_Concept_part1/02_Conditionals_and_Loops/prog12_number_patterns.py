# Program 1.24: Number Pattern
# Print the following number pattern for 5 rows:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Then print it in reverse (descending). Use nested loops.

rows = 5

print("--- Number Pattern (Ascending) ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n--- Number Pattern (Descending) ---")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
