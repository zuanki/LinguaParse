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
        analyzed_text = []
        paragraphs = text.split('\n')
        print(len(paragraphs))
        for p in paragraphs:
            words, tagged_words = self.strategy.analyze_text(p)

            for word, tag in tagged_words:
                pronounce = 'N/A'
                definition = 'N/A'
                # definition = self.strategy.get_definition(word)
                # pronounce = self.strategy.get_pronounce(word)
                analyzed_text.append({
                    'word': word,
                    'pos': tag,
                    'pronounce': pronounce,
                    'definition': definition
                })
                
            analyzed_text.append({
                    'word': '\n',
                    'pos': '改行',
                    'pronounce': 'かいぎょう',
                    'definition': 'Enter'
                })

        return analyzed_text
