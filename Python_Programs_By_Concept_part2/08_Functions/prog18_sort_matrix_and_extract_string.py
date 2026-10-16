# Program: Matrix Sorting & String Extraction Functions
# 1. sort_matrix(M) - sorts list of lists
#    Eg. M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]] -> [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# 2. extract_string(str_list1, l) - extracts strings with length >= l

def sort_matrix(M):
    return sorted(M)

def extract_string(str_list1, l):
    result = [s for s in str_list1 if len(s) >= l]
    return result

# Test sort_matrix
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sorted_mat = sort_matrix(matrix)
print("Original Matrix:", matrix)
print("Sorted Matrix  :", sorted_mat)

# Test extract_string
words = ['Python', 'list', 'exercises', 'practice', 'solution']
length_threshold = 8
extracted = extract_string(words, length_threshold)
print(f"\nStrings with length >= {length_threshold}:", extracted)
