# Program 3.4: Tuple Operations & Immutability Demonstration
# 1. Indexing, slicing, len(), unpacking (min, max, avg)
# 2. Demonstrate TypeError when trying to modify tuple
# 3. Convert to list, modify, and convert back to tuple

marks = (75, 82, 90, 68, 88)
print("Original Marks Tuple:", marks)

# Indexing and Slicing
print("First mark (index 0):", marks[0])
print("Last mark (index -1):", marks[-1])
print("Slice (index 1 to 3):", marks[1:4])
print("Length of tuple     :", len(marks))

# Unpacking
m1, m2, m3, m4, m5 = marks
print(f"Unpacked variables: m1={m1}, m2={m2}, m3={m3}, m4={m4}, m5={m5}")

# Immutability Demonstration
print("\nTrying to modify tuple directly (marks[0] = 95)...")
try:
    marks[0] = 95
except TypeError as e:
    print("Caught expected TypeError:", e)
    print("Reason: Tuples in Python are immutable!")

# Workaround: Convert to list, modify, convert back
temp_list = list(marks)
temp_list[0] = 95  # updating first mark
marks = tuple(temp_list)

print("\nAfter converting to list, modifying, and converting back:")
print("Updated tuple:", marks)
