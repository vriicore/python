# Practical Exam Task 12:
# Accept two lists of equal size and create a third list containing the sum of corresponding elements.

list1 = [5, 10, 15, 20, 25]
list2 = [10, 20, 30, 40, 50]

print("List 1:", list1)
print("List 2:", list2)

if len(list1) == len(list2):
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    print("\nThird List (Sum of corresponding elements):")
    print(sum_list)
else:
    print("Lists are not of equal size!")
