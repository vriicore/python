# Practical Exam Task 9:
# Write a menu-driven program to perform all list operations:
# - Append
# - Insert
# - Extend
# - Remove
# - Pop
# - Sort
# - Reverse
# - Count
# - Index
# - Copy
# - Clear
# - Display

data = [10, 20, 30]

while True:
    print("\n================ ALL LIST OPERATIONS MENU ================")
    print(" 1. Append   2. Insert   3. Extend   4. Remove   5. Pop")
    print(" 6. Sort     7. Reverse  8. Count    9. Index   10. Copy")
    print("11. Clear   12. Display 13. Exit")
    print("==========================================================")

    choice = input("Enter choice (1-13): ")

    if choice == "1":
        val = int(input("Enter value to append: "))
        data.append(val)
        print("Updated list:", data)
    elif choice == "2":
        idx = int(input("Enter index to insert at: "))
        val = int(input("Enter value: "))
        data.insert(idx, val)
        print("Updated list:", data)
    elif choice == "3":
        items = input("Enter space-separated values to extend: ").split()
        data.extend([int(x) for x in items])
        print("Updated list:", data)
    elif choice == "4":
        val = int(input("Enter value to remove: "))
        if val in data:
            data.remove(val)
            print(f"Removed {val}. List: {data}")
        else:
            print("Value not found!")
    elif choice == "5":
        if data:
            print("Popped element:", data.pop())
            print("Current list:", data)
        else:
            print("List is already empty!")
    elif choice == "6":
        data.sort()
        print("Sorted list:", data)
    elif choice == "7":
        data.reverse()
        print("Reversed list:", data)
    elif choice == "8":
        val = int(input("Enter value to count: "))
        print(f"Element {val} appears {data.count(val)} time(s).")
    elif choice == "9":
        val = int(input("Enter value to find index: "))
        if val in data:
            print(f"First occurrence index: {data.index(val)}")
        else:
            print("Value not found!")
    elif choice == "10":
        copied = data.copy()
        print("Copied list:", copied)
    elif choice == "11":
        data.clear()
        print("List cleared!")
    elif choice == "12":
        print("Current List:", data)
    elif choice == "13":
        print("Exiting list operations. Goodbye!")
        break
    else:
        print("Invalid option! Please enter 1 to 13.")
