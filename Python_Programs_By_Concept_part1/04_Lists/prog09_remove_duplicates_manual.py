# Program: Remove Duplicates Without set()
# Accept a list of integers from user and remove duplicates without using set().

sample = [1, 2, 3, 3, 3, 4, 2, 5, 1, 6]
print("Input List:", sample)

unique_list = []
for item in sample:
    if item not in unique_list:
        unique_list.append(item)

print("Unique List (Duplicates removed):", unique_list)
