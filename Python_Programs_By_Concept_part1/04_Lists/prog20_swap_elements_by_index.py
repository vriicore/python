# Program: Swap Two Elements at Given Positions
# Write a program to swap two elements in a list at user-specified indices.

my_list = [10, 20, 30, 40, 50, 60]
print("Original List:", my_list)

pos1 = int(input("Enter first index to swap (0 to 5): "))
pos2 = int(input("Enter second index to swap (0 to 5): "))

if 0 <= pos1 < len(my_list) and 0 <= pos2 < len(my_list):
    # swapping using python tuple assignment
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
    print(f"List after swapping indices {pos1} and {pos2}:", my_list)
else:
    print("Invalid index entered!")
