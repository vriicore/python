# Program: Second Largest and Second Smallest Without Built-in Sort
# Find the second largest and second smallest element in a list.

nums = [12, 45, 2, 45, 89, 34, 89, 7, 2]
print("Original list:", nums)

# remove duplicates first to get distinct values
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)

if len(unique) < 2:
    print("List must have at least two distinct values.")
else:
    # manual sorting (bubble sort)
    for i in range(len(unique)):
        for j in range(0, len(unique) - i - 1):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]

    second_smallest = unique[1]
    second_largest = unique[-2]

    print("Sorted unique list:", unique)
    print("Second Smallest element:", second_smallest)
    print("Second Largest element :", second_largest)
