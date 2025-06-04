from collections import Counter
import re

def word_frequency_counter(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    return word_counts

text = "This is a sample text. This text is just an example."
word_counts = word_frequency_counter(text)

for word, count in word_counts.items():
    print(f"{word}: {count}")