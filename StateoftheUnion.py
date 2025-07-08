import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('state_union')
nltk.download('punkt')

def count_words(text, words_to_count):
    """Counts occurrences of specific words in a text."""
    tokens = word_tokenize(text.lower())
    word_counts = Counter(tokens)
    return {word: word_counts[word] for word in words_to_count}

words_to_count = ["men", "women", "people"]
word_counts_by_year = {}

for fileid in state_union.fileids():
    year = fileid[:4]
    text = state_union.raw(fileid)
    counts = count_words(text, words_to_count)
    word_counts_by_year.setdefault(year, {}).update(counts)

for year, counts in word_counts_by_year.items():
  print(f"Year: {year}, Counts: {counts}")
