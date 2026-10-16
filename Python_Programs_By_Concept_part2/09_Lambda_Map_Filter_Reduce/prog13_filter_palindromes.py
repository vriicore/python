# Program: Filter Palindrome Words
# Take a list of words and print all palindrome words using filter() and slicing.

words = ["madam", "python", "racecar", "hello", "level", "radar", "world"]

palindromes = list(filter(lambda w: w == w[::-1], words))

print("Word list   :", words)
print("Palindromes :", palindromes)
