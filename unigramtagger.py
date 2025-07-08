import nltk
from nltk.tag import UnigramTagger
from nltk.corpus import treebank

train_data = treebank.tagged_sents()[:3000] # Use first 3000 sentences for training

unigram_tagger = UnigramTagger(train_data)

test_data = treebank.tagged_sents()[3000:] # Use the rest for testing
accuracy = unigram_tagger.evaluate(test_data)
print(f"Accuracy: {accuracy}")



sentence = ["This", "is", "a", "sample", "sentence", "."]
tagged_sentence = unigram_tagger.tag(sentence)
print(tagged_sentence)