# Program: Merge Two Lists and Sort Without sort()
# Write a program to merge two lists and sort in ascending/descending order
# without using built-in sort() (using Bubble Sort).

list1 = [64, 25, 12]
list2 = [22, 11, 90]

# merging
merged = list1 + list2
print("Merged list:", merged)

# Bubble sort for ascending order
asc_list = merged.copy()
n = len(asc_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if asc_list[j] > asc_list[j + 1]:
            # swap
            asc_list[j], asc_list[j + 1] = asc_list[j + 1], asc_list[j]

print("Sorted Ascending (without sort()):", asc_list)

# Descending order
desc_list = asc_list[::-1]
print("Sorted Descending:", desc_list)
