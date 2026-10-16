# Program: Separate 15 Numbers into Even and Odd Lists
# Accept 15 numbers, separate them into even and odd lists,
# and display their count, sum, max, and min values.

# Sample 15 numbers
nums = [12, 7, 19, 24, 33, 40, 55, 62, 71, 88, 90, 11, 4, 15, 28]
print("All 15 numbers:", nums)

even_list = []
odd_list = []

for n in nums:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("\n--- EVEN NUMBERS LIST ---")
print("List :", even_list)
print("Count:", len(even_list))
print("Sum  :", sum(even_list))
print("Max  :", max(even_list))
print("Min  :", min(even_list))

print("\n--- ODD NUMBERS LIST ---")
print("List :", odd_list)
print("Count:", len(odd_list))
print("Sum  :", sum(odd_list))
print("Max  :", max(odd_list))
print("Min  :", min(odd_list))
