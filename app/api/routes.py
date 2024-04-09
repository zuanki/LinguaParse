from flask import request, jsonify
from app.models import text_analyzer

SUPPORTED_LANGUAGES = ['en', 'ja']


def register_routes(app):
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'Hello world!'})
    
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

        if language not in SUPPORTED_LANGUAGES:
            return jsonify({'error': 'Unsupported language'}), 400

        analyzer = text_analyzer.TextAnalyzer(language)

        return jsonify(analyzer.analyze_text(text))
