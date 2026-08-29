import pdfplumber

def extract_text_from_pdf(uploaded_file):
    text=''
    with pdfplumber.open(uploaded_file) as pdf:
        for p in pdf.pages:
            t=p.extract_text()
            if t:text += t+'
'
    return text
