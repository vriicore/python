# Practical Exam Task 15:
# Write a program to find the second largest and second smallest element
# in a list without using built-in sorting.

numbers = [12, 45, 2, 89, 34, 7, 89, 23, 2]
print("Original Numbers:", numbers)

# remove duplicates to work with distinct values
distinct = []
for n in numbers:
    if n not in distinct:
        distinct.append(n)

if len(distinct) < 2:
    print("List must have at least 2 distinct numbers.")
else:
    # manual bubble sort
    for i in range(len(distinct)):
        for j in range(0, len(distinct) - i - 1):
            if distinct[j] > distinct[j + 1]:
                distinct[j], distinct[j + 1] = distinct[j + 1], distinct[j]

    second_smallest = distinct[1]
    second_largest = distinct[-2]

    print("Sorted unique elements:", distinct)
    print("Second Smallest element:", second_smallest)
    print("Second Largest element :", second_largest)
