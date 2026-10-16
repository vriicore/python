# Program: Basic Operations Using map()
# 1. Double every element in a list
# 2. Find square of every number
# 3. Find cube of every number
# 4. Add 5 to every number
# 5. Convert list of strings into uppercase
# 6. Find length of every string

nums = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "date"]

doubled = list(map(lambda x: x * 2, nums))
squared = list(map(lambda x: x ** 2, nums))
cubed = list(map(lambda x: x ** 3, nums))
plus_5 = list(map(lambda x: x + 5, nums))
upper_words = list(map(lambda s: s.upper(), words))
word_lengths = list(map(lambda s: len(s), words))

print("Original Numbers:", nums)
print("Doubled         :", doubled)
print("Squared         :", squared)
print("Cubed           :", cubed)
print("Add 5           :", plus_5)
print("\nOriginal Words  :", words)
print("Uppercase       :", upper_words)
print("Word Lengths    :", word_lengths)
