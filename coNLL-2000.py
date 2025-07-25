import nltk
from nltk.corpus import conll2000

train_sents = conll2000.chunked_sents('train.txt')

print(train_sents[0])

np_train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
print(np_train_sents[0])

from nltk.chunk import conlltags2tree, tree2conlltags
iob_tuples = tree2conlltags(train_sents[0])
print(iob_tuples)
