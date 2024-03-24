from app import create_app, db
from app.models.dictionary import EnglishWord, JapaneseWord

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()

    # Check if tables are empty
    if not EnglishWord.query.all() and not JapaneseWord.query.all():
        # Add sample English words
        english_words = [
            EnglishWord(
                word='apple', definition='A fruit that grows on trees'),
            EnglishWord(word='book', definition='A written or printed work'),
            EnglishWord(word='car', definition='A vehicle with four wheels'),
        ]
        db.session.add_all(english_words)

        # Add sample Japanese words
        japanese_words = [
            JapaneseWord(word='りんご', definition='木に実る果物'),
            JapaneseWord(word='本', definition='文字が印刷されている物'),
            JapaneseWord(word='車', definition='四輪の乗り物'),
        ]
        db.session.add_all(japanese_words)

        # Commit changes
        db.session.commit()
    else:
        print("Tables are not empty. Skipping data insertion.")
