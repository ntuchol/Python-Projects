import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_gerunds(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    gerunds = [word for word, tag in tagged_tokens if tag == 'VBG']
    return gerunds

text = "The constant barking of the dog was annoying. Swimming in the ocean is fun."
gerunds = extract_gerunds(text)
print(gerunds)