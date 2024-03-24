from abc import ABC, abstractmethod


class TextAnalysis(ABC):
    @abstractmethod
    def analyze_text(self, text):
        # Tokenize the text
        # Tag the words with their part-of-speech
        pass

    @abstractmethod
    def get_definition(self, word):
        pass
