import os
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

SUPPORTED_EXTS = {'.pdf', '.png', '.jpg', '.jpeg', '.txt'}

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext in {'.png', '.jpg', '.jpeg'}:
        return extract_text_from_image(file_path)
    elif ext == '.txt':
        return extract_text_from_txt(file_path)
    else:
        raise ValueError('Unsupported file type')

# Placeholder for embedding and retrieval logic
def embed_text(text):
    # TODO: Call OpenAI or other embedding model
    return [0.0] * 1536  # Dummy vector

def retrieve_relevant_chunks(query, user_files):
    # TODO: Implement vector search over user files
    return "Relevant content from user files."

