# Program: Split List into Chunks of Size N
# Divide a list into sub-lists of size n.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print("Original list:", data)
print(f"Chunk size: {n}")

chunks = []
for i in range(0, len(data), n):
    chunks.append(data[i : i + n])

print("Resulting Chunks:", chunks)
