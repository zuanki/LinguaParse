import unittest
from app.models.text_analyzer import TextAnalyzer


class TestUtils(unittest.TestCase):
    def test_analyze_english_text(self):
        text = "This is a test sentence."
        analyzer = TextAnalyzer('en')
        analyzed_text = analyzer.analyze_text(text)
        self.assertIsInstance(analyzed_text, list)
        self.assertTrue(len(analyzed_text) > 0)
        for word in analyzed_text:
            self.assertIn('word', word)
            self.assertIn('pos', word)
            self.assertIn('definition', word)

    def test_analyze_japanese_text(self):
        text = "これはテストの文章です。"
        analyzer = TextAnalyzer('ja')
        analyzed_text = analyzer.analyze_text(text)
        self.assertIsInstance(analyzed_text, list)
        self.assertTrue(len(analyzed_text) > 0)
        for word in analyzed_text:
            self.assertIn('word', word)
            self.assertIn('pos', word)
            self.assertIn('definition', word)


if __name__ == '__main__':
    unittest.main()
