# Practical Exam Task 3:
# Create a shopping list.
# Implement a menu-driven program to add, remove, search, update, sort, and display items.

shopping_list = ["Notebook", "Pen", "Folder", "Calculator"]

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added to shopping list.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed.")
    else:
        print("Item not found in shopping list.")

def search_item():
    item = input("Enter item to search: ")
    if item in shopping_list:
        pos = shopping_list.index(item)
        print(f"'{item}' found at index {pos}.")
    else:
        print(f"'{item}' not found.")

def update_item():
    old_item = input("Enter item to replace: ")
    if old_item in shopping_list:
        new_item = input("Enter new item: ")
        idx = shopping_list.index(old_item)
        shopping_list[idx] = new_item
        print("Item updated.")
    else:
        print("Item not found.")

def sort_items():
    shopping_list.sort()
    print("Shopping list sorted alphabetically:")
    display_items()

def display_items():
    print("\n--- Current Shopping List ---")
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")

def main():
    while True:
        print("\n===== SHOPPING LIST MENU =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Sort Items")
        print("6. Display List")
        print("7. Exit")
        print("==============================")

        ch = input("Enter your choice (1-7): ")
        if ch == "1":
            add_item()
        elif ch == "2":
            remove_item()
        elif ch == "3":
            search_item()
        elif ch == "4":
            update_item()
        elif ch == "5":
            sort_items()
        elif ch == "6":
            display_items()
        elif ch == "7":
            print("Exiting Shopping List. Bye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
