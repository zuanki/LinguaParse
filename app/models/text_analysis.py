from abc import ABC, abstractmethod


class TextAnalysis(ABC):
    @abstractmethod
    def tokenize_text(self, text):
        pass

    @abstractmethod
    def pos_tag(self, words):
        pass

    @abstractmethod
    def get_definition(self, word):
        pass
