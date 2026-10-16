# Program 3.6: Word Frequency Counter Using Dictionary
# Count frequency of each word in a paragraph.
# Display words sorted by frequency (most common first).

paragraph = """Python is a popular programming language.
Python is used for web development, software development,
and machine learning. Python is easy to learn."""

# clean and split
words = paragraph.lower().replace(".", "").replace(",", "").split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# sort by frequency descending
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("--- Word Frequency (Most Common First) ---")
print(f"{'Word':<15}{'Frequency'}")
print("-" * 25)
for word, count in sorted_freq:
    print(f"{word:<15}{count}")
