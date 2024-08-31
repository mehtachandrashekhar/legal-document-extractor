from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def train_classification_model(X_train, y_train):
    """
    Train a Naive Bayes text classification model.
    Args:
        X_train (list): List of preprocessed text documents for training.
        y_train (list): Corresponding labels for the training data.
    Returns:
        Pipeline: Trained model pipeline including vectorization and classification.
    """
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    return model

def predict_document_type(model, X_test):
    """
    Predict the document type using the trained classification model.
    Args:
        model (Pipeline): Trained model pipeline.
        X_test (list): List of preprocessed text documents for testing.
    Returns:
        list: Predicted labels for the test data.
    """
    return model.predict(X_test)
