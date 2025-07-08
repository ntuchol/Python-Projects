from nltk.corpus import brown
from collections import Counter

# Get all words from the Brown Corpus
words = brown.words()

# Count the frequency of each word
word_counts = Counter(words)

# Find words that appear at least three times
words_at_least_three = [word for word, count in word_counts.items() if count >= 3]

# Print the words (optional)
print(words_at_least_three)

# You can also sort the words by frequency if you prefer
sorted_words = sorted(words_at_least_three, key=word_counts.get, reverse=True)
print(sorted_words)