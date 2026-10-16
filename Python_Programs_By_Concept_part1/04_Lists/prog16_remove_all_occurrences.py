# Program: Remove All Occurrences of a Specific Value
# Remove all instances of a target element from list.

data = [5, 2, 8, 5, 1, 5, 9, 5]
val_to_remove = 5
print("Original list:", data)
print("Value to remove:", val_to_remove)

# student approach using list comprehension or while loop
cleaned = [x for x in data if x != val_to_remove]

print("List after removing all occurrences:", cleaned)
