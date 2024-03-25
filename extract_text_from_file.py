from docx import Document

def extract_text_from_docx(file_path):
    # The function extracts text from docx file
    #   Input: file_path - file path of the source docx document

    # Initialization
    doc = Document(file_path)
    full_text = []

    # Extract text
    for para in doc.paragraphs:
        full_text.append(para.text)


    return '\n'.join(full_text)
