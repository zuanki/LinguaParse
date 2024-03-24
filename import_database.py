import json
from app import create_app, db
from app.models.dictionary import EnglishWord, JapaneseWord
from tqdm import tqdm

app = create_app()


with app.app_context():
    # Create all tables
    db.create_all()

    # Import data from JSON file
    with open('data/english_dictionary.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Insert data into english_words table
    english_words = [
        EnglishWord(word=word, definition=definition)
        for word, definition in tqdm(data.items())
    ]

    db.session.add_all(english_words)

    # Add some sample Japanese words
    japanese_words = [
        JapaneseWord(word='りんご', definition='木に実る果物'),
        JapaneseWord(word='本', definition='文字が印刷されている物'),
        JapaneseWord(word='車', definition='四輪の乗り物'),
    ]

    db.session.add_all(japanese_words)

    # Commit changes
    db.session.commit()
    print("Data has been imported successfully.")
