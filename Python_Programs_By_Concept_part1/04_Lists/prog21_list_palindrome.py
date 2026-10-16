# Program: Check if List is Palindrome Without String Conversion
# Check whether a list reads the same forwards and backwards.

# Test lists
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

def check_palindrome(lst):
    # using two pointers
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True

print(f"List {list1} is palindrome? -> {check_palindrome(list1)}")
print(f"List {list2} is palindrome? -> {check_palindrome(list2)}")
