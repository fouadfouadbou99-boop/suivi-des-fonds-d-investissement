import streamlit as st
import pandas as pd

from pdf_reader import extract_text_from_pdf
from docx_reader import extract_text_from_docx
from extractor import analyze_document


st.set_page_config(
    page_title="Suivi Fonds PE et OPCI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Suivi des Fonds PE et OPCI")

try:
    st.write(
        f"GEMINI_API_KEY configurée : {'✅ Oui' if st.secrets.get('GEMINI_API_KEY') else '❌ Non'}"
    )
except Exception:
    st.write("GEMINI_API_KEY configurée : ❌ Non")


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

        st.error("Format non supporté")
        st.stop()

    st.success(
        f"Texte extrait : {len(text)} caractères"
    )

    with st.expander("Aperçu du texte extrait"):

        st.text_area(
            "Contenu",
            text[:5000],
            height=300
        )

    with st.spinner(
        "Analyse du document en cours..."
    ):

        result = analyze_document(text)

    st.success("Analyse terminée")

    ####################################################
    # SYNTHESE EXECUTIVE
    ####################################################

    infos = result.get(
        "informations_generales",
        {}
    )

    performance = result.get(
        "performance",
        {}
    )

    gouvernance = result.get(
        "gouvernance",
        {}
    )

    st.header("📌 Synthèse Exécutive")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Fonds",
            infos.get(
                "nom_du_fonds",
                "N/A"
            )
        )

    with col2:
        st.metric(
            "Taille du Fonds",
            infos.get(
                "taille_totale_du_fonds",
                "N/A"
            )
        )

    with col3:
        st.metric(
            "TRI",
            performance.get(
                "tri",
                "N/A"
            )
        )

    with col4:
        st.metric(
            "Date Comité",
            gouvernance.get(
                "date_reunion_comite_surveillance",
                "N/A"
            )
        )

    ####################################################
    # INFORMATIONS GENERALES
    ####################################################

    st.header("🏦 Informations Générales")

    st.write(
        f"**Nom du Fonds :** {infos.get('nom_du_fonds', 'N/A')}"
    )

    st.write(
        f"**Forme juridique :** {infos.get('forme_juridique', 'N/A')}"
    )

    st.write(
        f"**Nature des investissements :** {infos.get('nature_des_investissements', 'N/A')}"
    )

    st.write(
        f"**Date de constitution :** {infos.get('date_de_constitution', 'N/A')}"
    )

    st.write(
        f"**Durée du fonds :** {infos.get('duree_du_fonds', 'N/A')}"
    )

    ####################################################
    # ACTIONNARIAT
    ####################################################

    actionnariat = infos.get(
        "actionnariat",
        {}
    )

    if actionnariat:

        st.header("👥 Actionnariat")

        df_actionnariat = pd.DataFrame(
            list(actionnariat.items()),
            columns=[
                "Investisseur",
                "Participation"
            ]
        )

        st.dataframe(
            df_actionnariat,
            use_container_width=True
        )

    ####################################################
    # PERFORMANCE
    ####################################################

    st.header("📈 Performance")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Montant Investi",
            f"{performance.get('total_investi_dh', 'N/A')}"
        )

        st.metric(
            "TRI",
            performance.get(
                "tri",
                "N/A"
            )
        )

    with c2:

        st.metric(
            "Valorisation",
            f"{performance.get('valorisation_portefeuille_dh', 'N/A')}"
        )

        st.metric(
            "Valeur Liquidative",
            performance.get(
                "valeur_liquidative_actuelle_dh",
                "N/A"
            )
        )

    with c3:

        st.metric(
            "Plus-value",
            f"{performance.get('plus_value_totale_dh', 'N/A')}"
        )

        st.metric(
            "Progression VL",
            performance.get(
                "progression_valeur_liquidative",
                "N/A"
            )
        )

    ####################################################
    # PARTICIPATIONS
    ####################################################

    participations = result.get(
        "participations",
        []
    )

    if participations:

        st.header("🏢 Portefeuille de Participations")

        df_participations = pd.DataFrame(
            participations
        )

        st.dataframe(
            df_participations,
            use_container_width=True
        )

    ####################################################
    # ALERTES
    ####################################################

    alertes = result.get(
        "alertes",
        []
    )

    if alertes:

        st.header("🚨 Alertes")

        for alerte in alertes:

            st.warning(
                alerte
            )

    ####################################################
    # RISQUES
    ####################################################

    risques = result.get(
        "risques",
        []
    )

    if risques:

        st.header("⚠️ Risques")

        for risque in risques:

            st.error(
                risque
            )

    ####################################################
    # DECISIONS
    ####################################################

    decisions = result.get(
        "decisions",
        []
    )

    if decisions:

        st.header("✅ Décisions du Comité")

        for decision in decisions:

            st.success(
                decision
            )

    ####################################################
    # ACTIONS A MENER
    ####################################################

    actions = result.get(
        "actions_a_mener",
        []
    )

    if actions:

        st.header("📋 Actions de Suivi")

        for action in actions:

            st.info(
                action
            )

    ####################################################
    # GOUVERNANCE
    ####################################################

    st.header("🏛 Gouvernance")

    st.json(
        gouvernance
    )

    ####################################################
    # JSON COMPLET
    ####################################################

    with st.expander(
        "Afficher le JSON complet"
    ):

        st.json(result)
