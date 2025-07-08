import nltk
from nltk.corpus import brown

# Download the Brown Corpus data if you haven't already
nltk.download('brown')

# Access the categories within the corpus
print(brown.categories())

# Access words from a specific category
news_words = brown.words(categories='news')
print(news_words[:20])

# Access sentences from a specific category
news_sentences = brown.sents(categories='news')
print(news_sentences[0])