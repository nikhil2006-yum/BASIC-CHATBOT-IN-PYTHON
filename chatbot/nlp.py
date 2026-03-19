import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def process_input(text):
    tokens = word_tokenize(text.lower())
    return tokens
