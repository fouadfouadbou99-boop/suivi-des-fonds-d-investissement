import streamlit as st
from extraction.pdf_reader import extract_text_from_pdf
from extraction.docx_reader import extract_text_from_docx
from ai.extractor import analyze_document

st.set_page_config(page_title="Suivi Fonds PE et OPCI",page_icon="📊",layout="wide")
st.title("📊 Suivi des Fonds PE et OPCI")

uploaded_file = st.file_uploader("Déposer un reporting", type=["pdf","docx"])
if uploaded_file:
    if uploaded_file.name.lower().endswith('.pdf'):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)
    st.success(f"Texte extrait : {len(text)} caractères")
    with st.spinner('Analyse en cours...'):
        result = analyze_document(text)
    st.json(result)
