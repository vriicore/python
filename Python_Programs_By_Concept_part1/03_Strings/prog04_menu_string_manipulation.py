# Program: Menu-driven String Manipulation
# Options:
# 1. Find length of string
# 2. Print string in upper case
# 3. Print string in lower case
# 4. Print string with initial capital (Title case)
# 5. Split the string into words

user_str = input("Enter a sentence/string: ")

while True:
    print("\n===== STRING MANIPULATION MENU =====")
    print("1. Find Length of String")
    print("2. Convert to Upper Case")
    print("3. Convert to Lower Case")
    print("4. Convert to Title Case (Initial Capital)")
    print("5. Split the String")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Length:", len(user_str))
    elif choice == "2":
        print("Upper Case:", user_str.upper())
    elif choice == "3":
        print("Lower Case:", user_str.lower())
    elif choice == "4":
        print("Title Case:", user_str.title())
    elif choice == "5":
        print("Split Words:", user_str.split())
    elif choice == "6":
        print("Exiting String Menu.")
        break
    else:
        print("Invalid choice! Please select 1 to 6.")
