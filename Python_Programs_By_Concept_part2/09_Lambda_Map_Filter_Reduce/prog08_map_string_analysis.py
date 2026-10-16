# Program: String Word Analysis Using map()
# Analyze string words: display uppercase with length and vowel count per word.

text = "Hello how are you"
words = text.split()

def analyze_word(word):
    upper = word.upper()
    length = len(word)
    vowel_counts = {}
    for ch in word.lower():
        if ch in 'aeiou':
            vowel_counts[ch] = vowel_counts.get(ch, 0) + 1
    vowel_list = [{v: c} for v, c in vowel_counts.items()]
    return {upper: vowel_list, "length": length}

analysis = list(map(analyze_word, words))

print("Input Sentence:", text)
print("Analysis Output:")
print(analysis)
