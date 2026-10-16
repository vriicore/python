# Program: Replace Character Without using replace()
# Copy inputted string to another string by replacing character 'o' with '@'.
# E.g. 'Hello' -> 'Hell@', 'Good Morning' -> 'G@@d M@rning'.

original = input("Enter a string: ")
result = ""

for ch in original:
    if ch == 'o' or ch == 'O':
        result += '@'
    else:
        result += ch

print("Original string :", original)
print("Modified string :", result)
