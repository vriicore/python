# Program: Chained map() and filter() Programs
# 1. Squares of only even numbers
# 2. Cubes of numbers divisible by 3
# 3. Filter salaries > 40000 and increase by 10%
# 4. Filter passed students (marks >= 40) and sort by marks

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

# 1. Squares of even
sq_even = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

# 2. Cubes of div by 3
cube_div3 = list(map(lambda x: x**3, filter(lambda x: x % 3 == 0, nums)))

# 3. Salaries > 40000 with 10% raise
salaries = [35000, 42000, 50000, 38000, 60000]
raised = list(map(lambda s: s * 1.10, filter(lambda s: s > 40000, salaries)))

# 4. Passed students sorted
marks = [75, 32, 88, 25, 92, 45]
passed_sorted = sorted(filter(lambda m: m >= 40, marks), reverse=True)

print("Squares of Even Numbers      :", sq_even)
print("Cubes of Numbers Div by 3    :", cube_div3)
print("Salaries > 40k with 10% raise:", [round(x) for x in raised])
print("Passed Marks (High to Low)   :", passed_sorted)
