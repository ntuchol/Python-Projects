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
    # Convert to lowercase and remove punctuation
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text) # Removes non-alphanumeric characters except whitespace

    # Split the text into words
    words = cleaned_text.split()

    # Count word frequencies
    word_counts = Counter(words)
    return word_counts

# Example usage
sample_text = "This is a sample text. This text is for demonstrating word frequency counting."
frequencies = count_word_frequencies(sample_text)
print(frequencies)