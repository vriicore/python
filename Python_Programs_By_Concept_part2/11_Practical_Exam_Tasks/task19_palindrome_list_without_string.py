# Practical Exam Task 19:
# Accept a list and check whether it is a palindrome without converting it into a string.

# Sample test lists
list1 = [10, 20, 30, 20, 10]
list2 = [1, 2, 3, 4, 5]

def is_palindrome_list(lst):
    # Two-pointer approach comparing list elements directly
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True

print(f"List 1: {list1} -> Palindrome: {is_palindrome_list(list1)}")
print(f"List 2: {list2} -> Palindrome: {is_palindrome_list(list2)}")

# User input testing
user_inp = input("\nEnter space-separated elements to test your list: ")
if user_inp.strip():
    user_list = user_inp.split()
    print("Your List:", user_list)
    if is_palindrome_list(user_list):
        print("Result: The list IS a Palindrome!")
    else:
        print("Result: The list is NOT a Palindrome.")
