# Program: Comprehensive List Comprehensions
# Create:
# 1. Squares of numbers 1-20
# 2. Even numbers 1-50
# 3. Words longer than 5 letters from sentence
# 4. Cubes of odd numbers 1-15
# 5. Multiplication table for 5
# 6. Numbers divisible by 3 and 5 up to 100
# 7. Assign grades based on marks

# 1. Squares 1-20
squares = [x**2 for x in range(1, 21)]
print("1. Squares 1-20:", squares)

# 2. Evens 1-50
evens = [x for x in range(1, 51) if x % 2 == 0]
print("2. Evens 1-50:", evens[:10], "... (total 25)")

# 3. Words longer than 5 letters
sentence = "Python programming list comprehension exercises are very interesting"
long_words = [w for w in sentence.split() if len(w) > 5]
print("3. Words > 5 chars:", long_words)

# 4. Cubes of odds 1-15
odd_cubes = [x**3 for x in range(1, 16) if x % 2 != 0]
print("4. Cubes of odd numbers 1-15:", odd_cubes)

# 5. Multiplication table of 5
table_5 = [5 * i for i in range(1, 11)]
print("5. Table of 5:", table_5)

# 6. Divisible by 3 and 5 up to 100
div_3_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("6. Divisible by 3 and 5:", div_3_5)

# 7. Grades
marks_list = [95, 82, 67, 54, 30]
grades = ['A' if m >= 90 else 'B' if m >= 75 else 'C' if m >= 50 else 'Fail' for m in marks_list]
print("7. Marks :", marks_list)
print("   Grades:", grades)
