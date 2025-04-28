def english_to_french_dict(english_words, french_words):
    """
    Creates an English-to-French dictionary.

    Args:
        english_words: A list of English words.
        french_words: A list of corresponding French words.

    Returns:
        A dictionary with English words as keys and French words as values.
    """
    if len(english_words) != len(french_words):
        raise ValueError("The lists of English and French words must have the same length.")

    return dict(zip(english_words, french_words))

# Example usage:
english_words = ["hello", "goodbye", "thank you", "please"]
french_words = ["bonjour", "au revoir", "merci", "s'il vous plaît"]

en_fr_dict = english_to_french_dict(english_words, french_words)
print(en_fr_dict)
# Expected Output: {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci', 'please': "s'il vous plaît"}

# Accessing values:
print(en_fr_dict["hello"])  # Output: bonjour

# Handling missing keys:
try:
    print(en_fr_dict["cat"])
except KeyError:
    print("Word not found in dictionary.")