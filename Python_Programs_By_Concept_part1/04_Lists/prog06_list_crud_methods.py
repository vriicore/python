# Program: Append, Insert, Remove and Pop Operations
# Demonstrate basic list modification functions.

items = ["apple", "banana", "cherry"]
print("Initial list:", items)

# append
items.append("mango")
print("After append('mango'):", items)

# insert at index 1
items.insert(1, "orange")
print("After insert(1, 'orange'):", items)

# remove by value
items.remove("banana")
print("After remove('banana'):", items)

# pop last item
popped = items.pop()
print(f"After pop() (removed {popped}):", items)

# pop at specific index
popped_idx = items.pop(0)
print(f"After pop(0) (removed {popped_idx}):", items)
