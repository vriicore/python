# Practical Exam Task 14:
# Accept a list of integers and rotate the list by k positions (left and right).

numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original List:", numbers)

k = int(input("Enter rotation positions (k): "))

# normalize k
k = k % len(numbers)

# Left rotation (elements shift to left)
left_rotated = numbers[k:] + numbers[:k]

# Right rotation (elements shift to right)
right_rotated = numbers[-k:] + numbers[:-k]

print(f"\nLeft Rotated by {k} positions :", left_rotated)
print(f"Right Rotated by {k} positions:", right_rotated)
