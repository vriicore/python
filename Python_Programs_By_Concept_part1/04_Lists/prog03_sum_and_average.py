# Program: Sum and Average Without Built-in sum()
# Write a program to sum all elements in a list and find average.

numbers = [10, 25, 30, 45, 50, 60]
print("Numbers list:", numbers)

total = 0
for val in numbers:
    total += val

avg = total / len(numbers)

print("Sum of elements     :", total)
print("Average of elements :", avg)
