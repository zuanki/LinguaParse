import nltk
import re
from .text_analysis import TextAnalysis
from .dictionary import get_word
import nagisa


class EnglishTextAnalysis(TextAnalysis):
    def __init__(self):
        # Initialize NLTK data
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

    def analyze_text(self, text):
        # Tokenize the text
        # Tag the words with their part-of-speech

        words = nltk.word_tokenize(text)
        tagged_words = nltk.pos_tag(words, tagset='universal')

        return words, tagged_words

    def get_definition(self, word):
        word_obj = get_word(word, 'en')
        if word_obj:
            return word_obj.definition
        else:
            return "Definition not found"


class JapaneseTextAnalysis(TextAnalysis):
    def analyze_text(self, text):
        # Tokenize the text
        # Tag the words with their part-of-speech

        words = nagisa.tagging(text)

        return words.words, [(word, tag) for word, tag in zip(words.words, words.postags)]

    def get_definition(self, word):
        word_obj = get_word(word, 'ja')
        if word_obj:
            return word_obj.definition
        else:
            return "Definition not found"
