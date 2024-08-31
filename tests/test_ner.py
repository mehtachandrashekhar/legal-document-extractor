import unittest
from src.ner import extract_entities

class TestNER(unittest.TestCase):
    def test_extract_entities(self):
        text = "John Doe vs State of XYZ under XYZ Act, Section 34."
        entities = extract_entities(text)
        self.assertIn(("John Doe", "PERSON"), entities)
        self.assertIn(("XYZ", "ORG"), entities)

if __name__ == '__main__':
    unittest.main()
