from nltk.corpus import brown
from collections import Counter

words = brown.words()

word_counts = Counter(words)

words_at_least_three = [word for word, count in word_counts.items() if count >= 3]

print(words_at_least_three)

sorted_words = sorted(words_at_least_three, key=word_counts.get, reverse=True)
print(sorted_words)
