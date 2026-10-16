# Program: Word Counter
# Count total number of words in the string input by user.

sentence = input("Enter a sentence: ")
words = sentence.split()
total_words = len(words)

print("List of words:", words)
print("Total number of words:", total_words)
