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

    st.info(
        f"Document chargé : {uploaded_file.name}"
    )

    if uploaded_file.name.lower().endswith(".pdf"):

        text = extract_text_from_pdf(
            uploaded_file
        )

    elif uploaded_file.name.lower().endswith(".docx"):

        text = extract_text_from_docx(
            uploaded_file
        )

    else:

        st.error(
            "Format de fichier non supporté"
        )

        st.stop()

    st.success(
        f"Texte extrait : {len(text)} caractères"
    )

    with st.expander(
        "Aperçu du texte extrait"
    ):

        st.text_area(
            "Contenu",
            text[:5000],
            height=300
        )

    with st.spinner(
        "Analyse du document en cours..."
    ):

        result = analyze_document(
            text
        )

    st.success(
        "Analyse terminée"
    )

    st.subheader(
        "Résultat"
    )

    st.json(result)
