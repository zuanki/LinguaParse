import nltk
import re
from .text_analysis import TextAnalysis
from .dictionary import get_word


class EnglishTextAnalysis(TextAnalysis):
    def __init__(self):
        # Initialize NLTK data
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

    def tokenize_text(self, text):
        return nltk.word_tokenize(text)

    def pos_tag(self, words):
        return nltk.pos_tag(words, tagset='universal')

    def get_definition(self, word):
        word_obj = get_word(word, 'en')
        if word_obj:
            return word_obj.definition
        else:
            return "Definition not found"


class JapaneseTextAnalysis(TextAnalysis):
    def tokenize_text(self, text):
        # TODO: Implement a tokenizer for Japanese text
        regex = r'[一-龠]+|[ぁ-ゔ]+|[ァ-ヴー]+|[a-zA-Z0-9]+|[ａ-ｚＡ-Ｚ０-９]+|[々〆〤ヶ]+'
        return re.findall(regex, text)

    def pos_tag(self, words):
        # TODO: Implement a part-of-speech tagger for Japanese text
        return [(word, 'NOUN') for word in words]

    def get_definition(self, word):
        word_obj = get_word(word, 'ja')
        if word_obj:
            return word_obj.definition
        else:
            return "Definition not found"
