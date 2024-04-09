from .language import EnglishTextAnalysis, JapaneseTextAnalysis


class TextAnalyzer:
    def __init__(self, language):
        if language == 'en':
            self.strategy = EnglishTextAnalysis()
        elif language == 'ja':
            self.strategy = JapaneseTextAnalysis()
        else:
            raise ValueError('Unsupported language')

    def analyze_text(self, text):
        words, tagged_words = self.strategy.analyze_text(text)
        analyzed_text = []

        for word, tag in tagged_words:
            definition = self.strategy.get_definition(word)
            pronounce = self.strategy.get_pronounce(word)
            analyzed_text.append({
                'word': word,
                'pos': tag,
                'pronounce': pronounce,
                'definition': definition
            })

        return analyzed_text
