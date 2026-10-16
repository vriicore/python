# Practical Exam Task 21:
# Accept a list of integers and find all missing numbers between the minimum and maximum values.

numbers = [10, 11, 14, 15, 18, 20]
print("Input List:", numbers)

min_val = min(numbers)
max_val = max(numbers)
print(f"Range is from {min_val} to {max_val}")

missing_numbers = []
for num in range(min_val, max_val + 1):
    if num not in numbers:
        missing_numbers.append(num)

print("\nMissing numbers between min and max:")
print(missing_numbers)
