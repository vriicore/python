# Practical Exam Task 5:
# Accept 15 numbers in a list.
# Separate them into even and odd lists and display their count, sum, maximum, and minimum values.

nums = [14, 23, 7, 42, 55, 68, 71, 80, 93, 16, 25, 38, 49, 60, 85]
print("15 Numbers List:", nums)

even_list = []
odd_list = []

for n in nums:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("\n--- EVEN NUMBERS ---")
print("List    :", even_list)
print("Count   :", len(even_list))
print("Sum     :", sum(even_list))
print("Maximum :", max(even_list))
print("Minimum :", min(even_list))

print("\n--- ODD NUMBERS ---")
print("List    :", odd_list)
print("Count   :", len(odd_list))
print("Sum     :", sum(odd_list))
print("Maximum :", max(odd_list))
print("Minimum :", min(odd_list))
