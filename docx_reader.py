from docx import Document

def extract_text_from_docx(uploaded_file):
    doc=Document(uploaded_file)
    return '
'.join(p.text for p in doc.paragraphs)
