# Practical Exam Task 16:
# Create a list of numbers and replace every negative number with zero.

numbers = [25, -5, 10, -18, 0, -32, 45, -2, 70]
print("Original Numbers List:", numbers)

modified_list = []
for n in numbers:
    if n < 0:
        modified_list.append(0)
    else:
        modified_list.append(n)

print("\nAfter replacing all negative numbers with zero:")
print(modified_list)
