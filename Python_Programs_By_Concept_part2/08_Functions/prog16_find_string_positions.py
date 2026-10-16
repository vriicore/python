# Program: findString Function with Default Argument
# Write findString(str1, str2='all') to find all positions of occurrences of str2 in str1.
# If not present, display suitable message.

def findString(str1, str2="all"):
    positions = []
    start = 0
    while True:
        pos = str1.find(str2, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + len(str2)

    if positions:
        print(f"String '{str2}' found at positions: {positions}")
        return positions
    else:
        print(f"String '{str2}' is not present in the given text.")
        return []

# Test
s1 = "Hello all, Good Morning to all."
print("Main string:", s1)

print("\n1. Using default argument 'all':")
findString(s1)

print("\n2. Searching custom word 'Good':")
findString(s1, "Good")

print("\n3. Searching absent word 'bye':")
findString(s1, "bye")
