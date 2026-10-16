# Practical Exam Task 22:
# Write a program to create a frequency table of elements in a list.

elements = [10, 20, 20, 30, 40, 10, 20, 50, 40, 10, 60]
print("List of Elements:", elements)

# build frequency dictionary
frequency_table = {}
for item in elements:
    if item in frequency_table:
        frequency_table[item] += 1
    else:
        frequency_table[item] = 1

# display frequency table
print("\n=============================")
print(f"{'Element':<15}{'Frequency'}")
print("=============================")
for item, count in sorted(frequency_table.items()):
    print(f"{item:<15}{count}")
print("=============================")
