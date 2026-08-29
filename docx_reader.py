from docx import Document


def extract_text_from_docx(uploaded_file):

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text
