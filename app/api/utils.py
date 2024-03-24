from app.models import english, japanese


def analyze_english_text(text):
    words = english.tokenize_text(text)
    tagged_words = english.pos_tag(words)
    analyzed_text = []

    for word, tag in tagged_words:
        definition = english.get_definition(word)
        analyzed_text.append({
            'word': word,
            'pos': tag,
            'definition': definition
        })

    return analyzed_text


def analyze_japanese_text(text):
    words = japanese.tokenize_text(text)
    tagged_words = japanese.pos_tag(words)
    analyzed_text = []

    for word, tag in tagged_words:
        definition = japanese.get_definition(word)
        analyzed_text.append({
            'word': word,
            'pos': tag,
            'definition': definition
        })

    return analyzed_text
