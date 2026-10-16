# Program: Membership Operators in Strings
# Take an input character from user and check whether that character is present in string:
# Using 'in' operator and using 'not in' operator.

main_str = input("Enter main string: ")
ch = input("Enter a single character to check: ")

# using 'in' operator
if ch in main_str:
    print(f"Using 'in': Character '{ch}' is PRESENT in the string.")
else:
    print(f"Using 'in': Character '{ch}' is NOT PRESENT in the string.")

# using 'not in' operator
if ch not in main_str:
    print(f"Using 'not in': Character '{ch}' is NOT present.")
else:
    print(f"Using 'not in': Character '{ch}' IS present.")
