from .base import db


class EnglishWord(db.Model):
    __tablename__ = 'english_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)
    definition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<EnglishWord {self.word}>'


class JapaneseWord(db.Model):
    __tablename__ = 'japanese_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)
    definition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<JapaneseWord {self.word}>'


def get_word(word, language):
    if language == 'en':
        return EnglishWord.query.filter_by(word=word).first()
    elif language == 'ja':
        return JapaneseWord.query.filter_by(word=word).first()
    else:
        return None
