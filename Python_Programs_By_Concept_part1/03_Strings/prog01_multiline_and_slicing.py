# Program: String practice - Multiline and Slicing
# 1. Print multiple lines using single print statement:
#    I like "Python Programming" very much
#    It is my favorite subject
# 2. Print "very much" using slice operator.
# 3. Print the last 5 characters.
# 4. Print only the second line.
# 5. Print the string in reverse order.

text = '''I like "Python Programming" very much
It is my favorite subject'''

print("--- 1. Original String ---")
print(text)

# Line 1: 'I like "Python Programming" very much'
first_line = text.splitlines()[0]
second_line = text.splitlines()[1]

# 2. Slice "very much"
idx = first_line.find("very much")
slice_part = first_line[idx : idx + len("very much")]
print("\n--- 2. Sliced 'very much' ---")
print(slice_part)

# 3. Last 5 characters of entire string
last_5 = text[-5:]
print("\n--- 3. Last 5 characters ---")
print(last_5)

# 4. Only second line
print("\n--- 4. Second Line ---")
print(second_line)

# 5. Reverse string
print("\n--- 5. Reversed String ---")
print(text[::-1])
