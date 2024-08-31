import spacy

# Load spaCy's pre-trained NER model
nlp = spacy.load("en_core_web_md")

def extract_entities(text):
    """
    Extract named entities from the text using a pre-trained spaCy model.
    Args:
        text (str): Preprocessed text.
    Returns:
        list: List of tuples containing extracted entities and their labels.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
