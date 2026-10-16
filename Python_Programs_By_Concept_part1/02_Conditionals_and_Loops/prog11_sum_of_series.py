# Program 1.23: Sum of Series
# Calculate:
# (a) Sum of first N natural numbers
# (b) Sum of squares (1^2 + 2^2 + ... + N^2)
# (c) Sum of cubes (1^3 + 2^3 + ... + N^3)
# Use for loops.

n = int(input("Enter value of N: "))

sum_natural = 0
sum_squares = 0
sum_cubes = 0

for i in range(1, n + 1):
    sum_natural += i
    sum_squares += i ** 2
    sum_cubes += i ** 3

print(f"--- Series Results for N = {n} ---")
print("1. Sum of first N natural numbers :", sum_natural)
print("2. Sum of squares (1^2 to N^2)     :", sum_squares)
print("3. Sum of cubes (1^3 to N^3)       :", sum_cubes)
