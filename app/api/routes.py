from flask import request, jsonify
from app.api import utils


def register_routes(app):
    @app.route('/api/v1/analyze', methods=['POST'])
    def analyze_text():
        # {
        #     "text": "This is a test message.",
        #     "language": "en"
        # }
        text = request.json.get('text')
        language = request.json.get('language')

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        if language == 'en':
            analyzed_text = utils.analyze_english_text(text)
        elif language == 'ja':
            analyzed_text = utils.analyze_japanese_text(text)
        else:
            return jsonify({'error': 'Unsupported language'}), 400

        return jsonify(analyzed_text)
