# Program: Complete Menu-Driven List Operations
# Supports: Append, Insert, Extend, Remove, Pop, Sort, Reverse, Count, Index, Copy, Clear, Display.

lst = [10, 20, 30]

while True:
    print("\n======== LIST OPERATIONS MENU ========")
    print("1. Append    2. Insert    3. Extend")
    print("4. Remove    5. Pop       6. Sort")
    print("7. Reverse   8. Count     9. Index")
    print("10. Copy     11. Clear    12. Display")
    print("13. Exit")
    print("=======================================")

    choice = input("Enter choice (1-13): ")

    if choice == "1":
        val = int(input("Enter value to append: "))
        lst.append(val)
        print("Updated list:", lst)
    elif choice == "2":
        idx = int(input("Enter index: "))
        val = int(input("Enter value: "))
        lst.insert(idx, val)
        print("Updated list:", lst)
    elif choice == "3":
        items = input("Enter comma separated values: ").split(",")
        lst.extend([int(x.strip()) for x in items])
        print("Updated list:", lst)
    elif choice == "4":
        val = int(input("Enter value to remove: "))
        if val in lst:
            lst.remove(val)
            print("Removed. Current list:", lst)
        else:
            print("Value not found!")
    elif choice == "5":
        if lst:
            print("Popped item:", lst.pop())
        else:
            print("List is empty!")
    elif choice == "6":
        lst.sort()
        print("Sorted list:", lst)
    elif choice == "7":
        lst.reverse()
        print("Reversed list:", lst)
    elif choice == "8":
        val = int(input("Enter value to count: "))
        print(f"{val} appears {lst.count(val)} times.")
    elif choice == "9":
        val = int(input("Enter value to find index: "))
        if val in lst:
            print("Index is:", lst.index(val))
        else:
            print("Value not found!")
    elif choice == "10":
        copied_lst = lst.copy()
        print("Copied list:", copied_lst)
    elif choice == "11":
        lst.clear()
        print("List cleared!")
    elif choice == "12":
        print("Current list:", lst)
    elif choice == "13":
        print("Exiting list operations.")
        break
    else:
        print("Invalid choice!")
