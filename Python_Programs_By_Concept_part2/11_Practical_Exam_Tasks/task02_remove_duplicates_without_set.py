# Practical Exam Task 2:
# Accept a list of integers from the user.
# Remove all duplicate elements without using a set and display the unique list.

# Taking comma-separated inputs from user
user_input = input("Enter integers separated by space (or press Enter for default): ")
if user_input.strip():
    numbers = [int(x) for x in user_input.split()]
else:
    numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

print("Input List:", numbers)

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List (without using set):", unique_list)
