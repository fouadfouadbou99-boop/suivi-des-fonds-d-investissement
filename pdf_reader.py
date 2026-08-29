from docx import Document


def extract_text_from_docx(uploaded_file):

    document = Document(uploaded_file)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    return text
