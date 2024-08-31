import streamlit as st
import requests
from pypdf import PdfReader
import pytesseract
from PIL import Image
import pdf2image
import io

# URL of the Flask API
FLASK_API_URL = "http://127.0.0.1:5000/extract"

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file using OCR if necessary.
    """
    images = pdf2image.convert_from_bytes(pdf_file.read())
    text = ""
    for i, image in enumerate(images):
        page_text = pytesseract.image_to_string(image)
        text += f"--- Page {i + 1} ---\n"
        text += page_text + "\n"
    return text

def main():
    st.title("Legal Document Extractor")

    st.write("Upload your legal document (PDF format) here:")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        document_text = extract_text_from_pdf(uploaded_file)

        st.write("### Extracted Text:")
        st.write(document_text)
        
        if st.button("Extract Information"):
            if document_text:
                # Send the document text to the Flask API
                response = requests.post(FLASK_API_URL, json={"document": document_text})
                
                if response.status_code == 200:
                    data = response.json()
                    st.write("### Extracted Information:")
                    
                    st.write("#### Entities:")
                    st.write(data.get("entities", "No entities found."))
                    
                    st.write("#### Legal References:")
                    st.write(data.get("legal_references", "No legal references found."))
                else:
                    st.error("Error: Unable to get response from the server.")
            else:
                st.error("No text extracted from the document.")
    else:
        st.info("Please upload a PDF file.")

if __name__ == "__main__":
    main()
