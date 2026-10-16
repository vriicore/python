# Practical Exam Task 7:
# Accept a sentence from the user, convert it into a list of words,
# count the occurrence of each word, and remove repeated words.

sentence = input("Enter a sentence: ")
if not sentence.strip():
    sentence = "python is fun and learning python makes programming fun"

# convert sentence to list of words (lowercase for consistency)
words = sentence.lower().split()
print("\nList of words:", words)

# count occurrence of each word
print("\n--- Word Frequency ---")
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

for word, count in freq.items():
    print(f"'{word}': {count} time(s)")

# remove repeated words preserving order
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("\nUnique words (repeated words removed):", unique_words)
