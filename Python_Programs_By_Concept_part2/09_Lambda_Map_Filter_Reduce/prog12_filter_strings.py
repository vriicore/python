# Program: Filter Strings
# 1. Words with > 5 characters
# 2. Names starting with 'A'
# 3. Strings containing 'a'
# 4. Remove empty strings
# 5. Filter vowels from string

words = ["Apple", "Aarav", "banana", "", "cat", "elephant", "dog", "", "Airplane"]

gt_5 = list(filter(lambda w: len(w) > 5, words))
start_A = list(filter(lambda w: w.startswith('A'), words))
contains_a = list(filter(lambda w: 'a' in w.lower(), words))
non_empty = list(filter(lambda w: w.strip() != "", words))

# filter vowels from string
sample_str = "Antigravity Python Programming"
vowels_only = list(filter(lambda ch: ch.lower() in 'aeiou', sample_str))

print("Words > 5 chars          :", gt_5)
print("Names starting with 'A'  :", start_A)
print("Containing 'a'           :", contains_a)
print("Non-empty strings        :", non_empty)
print("Vowels extracted         :", "".join(vowels_only))
