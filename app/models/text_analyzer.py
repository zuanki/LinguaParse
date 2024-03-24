from .english import EnglishTextAnalysis
from .japanese import JapaneseTextAnalysis


class TextAnalyzer:
    def __init__(self, language):
        if language == 'en':
            self.strategy = EnglishTextAnalysis()
        elif language == 'ja':
            self.strategy = JapaneseTextAnalysis()
        else:
            raise ValueError('Unsupported language')

    def analyze_text(self, text):
        words = self.strategy.tokenize_text(text)
        tagged_words = self.strategy.pos_tag(words)
        analyzed_text = []

        for word, tag in tagged_words:
            definition = self.strategy.get_definition(word)
            analyzed_text.append({
                'word': word,
                'pos': tag,
                'definition': definition
            })

        return analyzed_text
