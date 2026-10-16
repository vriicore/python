# Program: UDF for Unique List
# Write an UDF to return a list having only unique values by removing duplicate values.
# Eg. I/P: [1,2,3,3,3,3,4,5] -> O/P: [1, 2, 3, 4, 5]

def get_unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
output_list = get_unique_list(sample_list)

print("Input List :", sample_list)
print("Unique List:", output_list)
