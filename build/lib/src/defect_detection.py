import re

def detect_legal_references(text):
    """
    Detect and extract legal references (Act and Section) from the text.
    Args:
        text (str): Preprocessed text from legal documents.
    Returns:
        list: List of detected legal references.
    """
    pattern = r'\b(section\s+\d+|\bact\b\s+\w+\b)'
    matches = re.findall(pattern, text)
    return matches
