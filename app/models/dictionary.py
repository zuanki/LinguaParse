from .base import db


class EnglishWord(db.Model):
    __tablename__ = 'english_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    pronounce = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<EnglishWord {self.word}>'


class JapaneseWord(db.Model):
    __tablename__ = 'japanese_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    pronounce = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(100), nullable=True)
    definition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<JapaneseWord {self.word}>'


def get_word(word, language):
    if language == 'en':
        return EnglishWord.query.filter_by(word=word.lower()).first()
    elif language == 'ja':
        res = JapaneseWord.query.filter_by(word=word).first()
        if not res:
            res = JapaneseWord.query.filter_by(pronounce=word).first()
        return res
    else:
        return None
