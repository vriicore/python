# Practical Exam Task 23:
# Create a list using list comprehension for numbers from 1 to 100 and display:
# - Squares
# - Cubes
# - Even numbers
# - Odd numbers
# - Multiples of 5

# Numbers 1 to 100
numbers = list(range(1, 101))

# 1. Squares
squares = [x**2 for x in numbers]

# 2. Cubes
cubes = [x**3 for x in numbers]

# 3. Even numbers
evens = [x for x in numbers if x % 2 == 0]

# 4. Odd numbers
odds = [x for x in numbers if x % 2 != 0]

# 5. Multiples of 5
multiples_of_5 = [x for x in numbers if x % 5 == 0]

print("--- List Comprehension Results (1 to 100) ---")
print("1. First 10 Squares     :", squares[:10], "... total 100")
print("2. First 10 Cubes       :", cubes[:10], "... total 100")
print("3. Even Numbers (total) :", len(evens), "numbers ->", evens[:10], "...")
print("4. Odd Numbers (total)  :", len(odds), "numbers ->", odds[:10], "...")
print("5. Multiples of 5       :", multiples_of_5)
