import nltk
from nltk.corpus import brown

nltk.download('brown')

print(brown.categories())

news_words = brown.words(categories='news')
print(news_words[:20])

news_sentences = brown.sents(categories='news')
print(news_sentences[0])
