import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_extract_data(self):
        response = self.app.post('/extract', json={
            "document": "John Doe vs State of XYZ under XYZ Act, Section 34."
        })
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("entities", data)
        self.assertIn("legal_references", data)

if __name__ == '__main__':
    unittest.main()
