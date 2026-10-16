# Practical Exam Task 10:
# Accept a list of numbers and perform slicing operations to display:
# - First five elements
# - Last five elements
# - Alternate elements
# - Reverse list using slicing

# 10 sample numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List of numbers:", numbers)

# First five elements
first_five = numbers[:5]
print("\n1. First five elements    :", first_five)

# Last five elements
last_five = numbers[-5:]
print("2. Last five elements     :", last_five)

# Alternate elements (step 2)
alternate = numbers[::2]
print("3. Alternate elements     :", alternate)

# Reverse list using slicing
reversed_list = numbers[::-1]
print("4. Reversed using slicing :", reversed_list)
