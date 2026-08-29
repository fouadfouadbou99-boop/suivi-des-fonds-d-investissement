import streamlit as st

from pdf_reader import extract_text_from_pdf
from docx_reader import extract_text_from_docx
from extracteur import analyze_document


st.set_page_config(
    page_title="Suivi Fonds PE et OPCI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Suivi des Fonds PE et OPCI")

uploaded_file = st.file_uploader(
    "Déposer un reporting",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    if uploaded_file.name.lower().endswith(".pdf"):

        text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.lower().endswith(".docx"):

        text = extract_text_from_docx(uploaded_file)

    else:

        st.error("Format non supporté")
        st.stop()

    st.success(
        f"Texte extrait : {len(text)} caractères"
    )

    result = analyze_document(text)

    st.json(result)
