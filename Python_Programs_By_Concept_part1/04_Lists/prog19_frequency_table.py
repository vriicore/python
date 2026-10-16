# Program: Frequency Table of Elements
# Write a program to find frequency of each element and build a dictionary/table.

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 2, 1]
print("Input list:", data)

freq = {}
for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("\n--- Element Frequency Table ---")
print(f"{'Element':<10}{'Count'}")
print("-" * 20)
for elem, count in freq.items():
    print(f"{elem:<10}{count}")
