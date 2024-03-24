import nltk

# Initialize NLTK data
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def tokenize_text(text):
    return nltk.word_tokenize(text)


def pos_tag(words):
    return nltk.pos_tag(words, tagset='universal')


def get_definition(word):
    # TODO Implement a function to get the definition of an English word
    return "Definition of " + word
