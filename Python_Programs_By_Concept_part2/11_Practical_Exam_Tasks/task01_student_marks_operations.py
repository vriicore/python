# Practical Exam Task 1:
# Create a list of 10 student marks.
# Perform insertion, deletion, updating, sorting, reversing,
# and display the highest, lowest, and average marks.

marks = [78, 85, 92, 65, 88, 70, 95, 82, 60, 75]
print("Initial 10 student marks:", marks)

# Insertion
marks.insert(2, 89)
print("\nAfter inserting 89 at index 2:", marks)

# Deletion
removed_mark = marks.pop(5)
print(f"After deleting mark {removed_mark} at index 5:", marks)

# Updating
marks[0] = 80
print("After updating mark at index 0 to 80:", marks)

# Sorting
marks.sort()
print("After sorting in ascending order:", marks)

# Reversing
marks.reverse()
print("After reversing (descending order):", marks)

# Highest, Lowest, and Average
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\n--- Summary Statistics ---")
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
print("Average Marks :", round(average, 2))
