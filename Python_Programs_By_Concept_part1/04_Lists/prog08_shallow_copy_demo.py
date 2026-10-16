# Program: Shallow Copy Demonstration
# Copy a list (shallow copy) and show it doesn't affect the original list.

original = [1, 2, 3, 4, 5]
# making a shallow copy using copy() or slicing
copied = original.copy()

print("Original before edit:", original)
print("Copied list         :", copied)

# modifying copied list
copied.append(99)
copied[0] = 100

print("\nAfter modifying copied list:")
print("Original list (unaffected):", original)
print("Copied list (modified)    :", copied)
