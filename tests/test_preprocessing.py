import unittest
from src.preprocessing import preprocess_text

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_text(self):
        raw_text = "IN THE SUPREME COURT OF INDIA\nCIVIL APPELLATE JURISDICTION"
        expected = "in the supreme court of india civil appellate jurisdiction"
        self.assertEqual(preprocess_text(raw_text), expected)

if __name__ == '__main__':
    unittest.main()
