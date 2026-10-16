# Program: Convert List of Strings to List of Integers
# Take a list of string numbers and convert each element to integer.

str_numbers = ["10", "25", "30", "42", "55"]
print("String list :", str_numbers)

int_numbers = []
for s in str_numbers:
    int_numbers.append(int(s))

print("Integer list:", int_numbers)
print("Sum of converted integers:", sum(int_numbers))
