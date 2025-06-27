import nltk
from nltk.corpus import conll2000

# Load the training set
train_sents = conll2000.chunked_sents('train.txt')

# Print the first chunked sentence
print(train_sents[0])

# Load only NP chunks
np_train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
print(np_train_sents[0])

# Example of converting to IOB format
from nltk.chunk import conlltags2tree, tree2conlltags
iob_tuples = tree2conlltags(train_sents[0])
print(iob_tuples)