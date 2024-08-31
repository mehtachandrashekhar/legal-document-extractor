import unittest
from src.classification import train_classification_model, predict_document_type

class TestClassification(unittest.TestCase):
    def test_classification_model(self):
        X_train = ["special leave petition", "writ petition"]
        y_train = ["Special Leave Petition", "Writ Petition"]
        model = train_classification_model(X_train, y_train)
        
        X_test = ["special leave petition"]
        prediction = predict_document_type(model, X_test)
        
        self.assertEqual(prediction[0], "Special Leave Petition")

if __name__ == '__main__':
    unittest.main()
