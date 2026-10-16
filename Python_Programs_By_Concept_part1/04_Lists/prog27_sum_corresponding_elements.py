# Program: Sum of Corresponding Elements of Two Lists
# Accept two lists of equal size and create a third list with sum of corresponding elements.

list_a = [1, 5, 10, 15, 20]
list_b = [9, 5, 20, 25, 30]

print("List A:", list_a)
print("List B:", list_b)

sum_list = []
for i in range(len(list_a)):
    sum_list.append(list_a[i] + list_b[i])

print("Sum of corresponding elements:", sum_list)
