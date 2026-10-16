# Program: Element Search and Frequency
# Write a program to:
# 1. Check if an element exists in a list
# 2. Count how many times a value appears
# 3. Find index of first and last occurrence

data = [10, 20, 30, 20, 40, 20, 50]
print("List:", data)

target = int(input("Enter number to search: "))

# check existence
if target in data:
    print(f"{target} is present in the list.")
    # count occurrences
    count = 0
    first_idx = -1
    last_idx = -1
    for i in range(len(data)):
        if data[i] == target:
            count += 1
            if first_idx == -1:
                first_idx = i
            last_idx = i
    print(f"Occurs {count} times.")
    print(f"First occurrence index: {first_idx}")
    print(f"Last occurrence index : {last_idx}")
else:
    print(f"{target} is NOT present in the list.")
