import re
from collections import Counter

def find_most_frequent_bigrams(text, n=50):
    words = re.findall(r'\b\w+\b', text.lower())
    
    bigrams = zip(words, words[1:])
    
    bigram_counts = Counter(bigrams)
    
    most_common_bigrams = bigram_counts.most_common(n)
    
    return most_common_bigrams

if __name__ == '__main__':
    text = """
    This is a sample text. This text is used to demonstrate 
    how to find the most frequent bigrams. Bigrams are pairs of 
    consecutive words, like 'this is' or 'is a'. This is a text.
    """
    
    most_frequent_50 = find_most_frequent_bigrams(text)

    print(f"The 50 most frequent bigrams are: \n")
    for bigram, count in most_frequent_50:
        print(f"{bigram}: {count}")
