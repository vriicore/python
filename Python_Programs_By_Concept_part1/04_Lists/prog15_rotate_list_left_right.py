# Program: Rotate List Left / Right by N Positions
# Rotate list left and right by k positions.

lst = [10, 20, 30, 40, 50, 60]
k = 2
print("Original list:", lst)
print("Rotate positions (k):", k)

# effective rotation
k = k % len(lst)

# left rotation: elements shift to left
left_rotated = lst[k:] + lst[:k]

# right rotation: elements shift to right
right_rotated = lst[-k:] + lst[:-k]

print("Left Rotated by 2 :", left_rotated)
print("Right Rotated by 2:", right_rotated)
