from flask import Flask, request, jsonify
from preprocessing import preprocess_text
from ner import extract_entities
from defect_detection import detect_legal_references

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the homepage!"

@app.route('/extract', methods=['POST'])
def extract_data():
    """
    API endpoint to process a legal document and extract relevant information.
    Expects a JSON payload with a 'document' field containing the text.
    Returns:
        JSON: Extracted entities and legal references.
    """
    data = request.json
    text = data.get('document', '')
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Extract entities
    entities = extract_entities(processed_text)
    
    # Detect legal references
    legal_references = detect_legal_references(processed_text)
    
    response = {
        "entities": entities,
        "legal_references": legal_references
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
