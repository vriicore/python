# Program: Count Uppercase and Lowercase Characters
# Write a function to calculate total number of Uppercase and lowercase characters in a string.

def count_case(text):
    upper_cnt = 0
    lower_cnt = 0
    for ch in text:
        if ch.isupper():
            upper_cnt += 1
        elif ch.islower():
            lower_cnt += 1
    return upper_cnt, lower_cnt

sample_string = "Hello World! Welcome to Python Programming."
u, l = count_case(sample_string)

print("String:", sample_string)
print("Total Uppercase characters:", u)
print("Total Lowercase characters:", l)
