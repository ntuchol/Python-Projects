from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Example usage
text = "The cats are running quickly. They were running faster than the dogs."
tokens = word_tokenize(text)
stemmed_text = stem_tokens(tokens)
print(stemmed_text)