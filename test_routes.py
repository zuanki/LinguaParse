from app import create_app
import json
import unittest


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_analyze_text_no_text(self):
        response = self.client.post(
            '/api/v1/analyze', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_analyze_text_unsupported_language(self):
        data = {'text': 'This is a test.', 'language': 'fr'}
        response = self.client.post(
            '/api/v1/analyze', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_analyze_english_text(self):
        data = {'text': 'This is a test.', 'language': 'en'}
        response = self.client.post(
            '/api/v1/analyze', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertTrue(len(response.json) > 0)

    def test_analyze_japanese_text(self):
        data = {'text': 'これはテストです。', 'language': 'ja'}
        response = self.client.post(
            '/api/v1/analyze', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertTrue(len(response.json) > 0)


if __name__ == '__main__':
    unittest.main()
