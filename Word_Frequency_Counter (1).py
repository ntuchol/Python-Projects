from collections import Counter
text = "This is a sample text. This text contains sample words."
    words = text.lower().split() # Convert to lowercase and split by spaces
    word_counts = Counter(words)
    print(word_counts)

    print(word_counts.most_common(3)) # Get the 3 most common words
    word_counts = {}
    text = "This is a sample text. This text contains sample words."
    words = text.lower().split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)


