# Program: Group Elements by Condition
# 1. Group numbers by Even / Odd
# 2. Group strings by word length

numbers = [12, 15, 22, 37, 40, 55, 68]
words = ["cat", "apple", "dog", "banana", "kiwi", "grape"]

# 1. Group numbers
grouped_numbers = {"Even": [], "Odd": []}
for n in numbers:
    if n % 2 == 0:
        grouped_numbers["Even"].append(n)
    else:
        grouped_numbers["Odd"].append(n)

# 2. Group words by length
grouped_words = {}
for w in words:
    l = len(w)
    if l not in grouped_words:
        grouped_words[l] = []
    grouped_words[l].append(w)

print("Numbers Grouped by Even/Odd:")
print(grouped_numbers)

print("\nWords Grouped by Length:")
for length, w_list in grouped_words.items():
    print(f"Length {length}: {w_list}")
