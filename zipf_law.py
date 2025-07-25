import re
import matplotlib.pyplot as plt
from collections import Counter

def zipf_law(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    ranks = range(1, len(sorted_word_counts) + 1)
    frequencies = [count for _, count in sorted_word_counts]

    plt.figure(figsize=(10, 6))
    plt.plot(ranks, frequencies)
    plt.xlabel("Rank(r)")
    plt.ylabel("Frequency(f)")
    plt.title("Zipf's Law")
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

text = """
zipf_law(text)
