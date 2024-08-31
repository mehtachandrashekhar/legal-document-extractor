import unittest

# Define the preprocess_text function here
def preprocess_text(text):
    # Example preprocessing: converting text to lowercase and removing newlines
    return " ".join(text.lower().split())

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_text(self):
        raw_text = "IN THE SUPREME COURT OF INDIA\nCIVIL APPELLATE JURISDICTION"
        expected = "in the supreme court of india civil appellate jurisdiction"
        self.assertEqual(preprocess_text(raw_text), expected)

if __name__ == '__main__':
    unittest.main()
