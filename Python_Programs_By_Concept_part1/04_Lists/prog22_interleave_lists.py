# Program: Interleave Two Lists
# E.g., [1, 3, 5] and [2, 4, 6] -> [1, 2, 3, 4, 5, 6]

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print("List 1:", l1)
print("List 2:", l2)

interleaved = []
len_min = min(len(l1), len(l2))

for i in range(len_min):
    interleaved.append(l1[i])
    interleaved.append(l2[i])

# append any remaining elements
interleaved.extend(l1[len_min:])
interleaved.extend(l2[len_min:])

print("Interleaved List:", interleaved)
