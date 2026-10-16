# Practical Exam Task 4:
# Write a program to merge two lists, remove duplicate elements,
# sort the final list, and display it in ascending and descending order.

list1 = [12, 45, 23, 89, 34]
list2 = [23, 67, 12, 90, 45, 11]

print("List 1:", list1)
print("List 2:", list2)

# Merge
merged = list1 + list2
print("Merged List:", merged)

# Remove duplicates without set
unique_list = []
for x in merged:
    if x not in unique_list:
        unique_list.append(x)

print("Duplicates Removed:", unique_list)

# Sort ascending
unique_list.sort()
print("Sorted in Ascending Order :", unique_list)

# Descending order
desc_list = unique_list[::-1]
print("Sorted in Descending Order:", desc_list)
