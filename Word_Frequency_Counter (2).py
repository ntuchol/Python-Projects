from collections import Counter
import re

def count_word_frequencies(text):
    """
    Counts the frequency of each word in a given text.

    Args:
        text (str): The input text.

    Returns:
        collections.Counter: A Counter object containing word frequencies.
    """
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text) # Removes non-alphanumeric characters except whitespace

    words = cleaned_text.split()

    word_counts = Counter(words)
    return word_counts

sample_text = "This is a sample text. This text is for demonstrating word frequency counting."
frequencies = count_word_frequencies(sample_text)
print(frequencies)
