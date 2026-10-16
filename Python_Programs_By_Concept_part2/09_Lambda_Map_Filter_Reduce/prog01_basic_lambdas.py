# Program: Basic Lambda Functions
# 1. Square of a number
# 2. Cube of a number
# 3. Maximum of two numbers
# 4. Maximum of three numbers
# 5. Check even or odd
# 6. Even multiplied by 5, odd multiplied by 10

square = lambda x: x ** 2
cube = lambda x: x ** 3
max_two = lambda a, b: a if a > b else b
max_three = lambda a, b, c: max_two(a, max_two(b, c))
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
even_odd_multiplier = lambda x: x * 5 if x % 2 == 0 else x * 10

print("Square of 6         :", square(6))
print("Cube of 4           :", cube(4))
print("Max of 15 and 27    :", max_two(15, 27))
print("Max of 10, 45, 30   :", max_three(10, 45, 30))
print("Check 7             :", check_even_odd(7))
print("Multiplier for 4    :", even_odd_multiplier(4))   # 4 * 5 = 20
print("Multiplier for 7    :", even_odd_multiplier(7))   # 7 * 10 = 70
