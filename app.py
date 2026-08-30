import streamlit as st
import pandas as pd

from pdf_reader import extract_text_from_pdf
from docx_reader import extract_text_from_docx
from extractor import analyze_document


def format_nombre(valeur):

    try:

        if valeur is None:
            return "N/A"

        return f"{int(valeur):,}".replace(",", " ")

    except Exception:

        return str(valeur)


st.set_page_config(
    page_title="Suivi Fonds PE et OPCI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Suivi Fonds PE & OPCI")

uploaded_file = st.file_uploader(
    "Déposer un reporting",
    type=["pdf", "docx"]
)

if uploaded_file:

    if uploaded_file.name.lower().endswith(".pdf"):

        text = extract_text_from_pdf(
            uploaded_file
        )

    else:

        text = extract_text_from_docx(
            uploaded_file
        )

    st.success(
        f"Texte extrait : {len(text)} caractères"
    )

    with st.spinner(
        "Analyse du reporting..."
    ):

        result = analyze_document(text)

    if "erreur" in result:

        st.error(result["erreur"])

        with st.expander("Détails"):

            st.json(result)

        st.stop()

    infos = result.get(
        "informations_generales",
        {}
    )

    perf = result.get(
        "performance",
        {}
    )

    gouvernance = result.get(
        "gouvernance",
        {}
    )

    #################################################
    # SYNTHESE EXECUTIVE
    #################################################

    st.header("📌 Synthèse Exécutive")

    synthese = result.get(
        "synthese_executive",
        ""
    )

    if synthese:

        st.info(synthese)

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
            perf.get(
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

    #################################################
    # ALERTES
    #################################################

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

    #################################################
    # RISQUES
    #################################################

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

    #################################################
    # DECISIONS
    #################################################

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

    #################################################
    # ACTIONS DE SUIVI
    #################################################

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

    #################################################
    # INFORMATIONS GENERALES
    #################################################

    st.header("🏦 Informations Générales")

    st.write(
        f"**Fonds :** {infos.get('nom_du_fonds','N/A')}"
    )

    st.write(
        f"**Forme juridique :** {infos.get('forme_juridique','N/A')}"
    )

    st.write(
        f"**Activité :** {infos.get('nature_des_investissements','N/A')}"
    )

    st.write(
        f"**Date de constitution :** {infos.get('date_de_constitution','N/A')}"
    )

    st.write(
        f"**Durée du Fonds :** {infos.get('duree_du_fonds','N/A')}"
    )

    #################################################
    # ACTIONNARIAT
    #################################################

    actionnariat = infos.get(
        "actionnariat",
        {}
    )

    if actionnariat:

        st.header("👥 Actionnariat")

        df_actionnaires = pd.DataFrame(
            list(actionnariat.items()),
            columns=[
                "Investisseur",
                "Participation"
            ]
        )

        st.dataframe(
            df_actionnaires,
            use_container_width=True
        )

    #################################################
    # PERFORMANCE
    #################################################

    st.header("📈 Performance")

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "Montant Investi",
            format_nombre(
                perf.get("total_investi_dh")
            )
        )

        st.metric(
            "TRI",
            perf.get(
                "tri",
                "N/A"
            )
        )

    with p2:

        st.metric(
            "Valorisation",
            format_nombre(
                perf.get(
                    "valorisation_portefeuille_dh"
                )
            )
        )

        st.metric(
            "Valeur liquidative",
            perf.get(
                "valeur_liquidative_actuelle_dh",
                "N/A"
            )
        )

    with p3:

        st.metric(
            "Valeur ajoutée",
            format_nombre(
                perf.get(
                    "plus_value_totale_dh"
                )
            )
        )

        st.metric(
            "Progression VL",
            perf.get(
                "progression_valeur_liquidative",
                "N/A"
            )
        )

    #################################################
    # PARTICIPATIONS
    #################################################

    participations = result.get(
        "participations",
        []
    )

    if participations:

        st.header(
            "🏢 Portefeuille de Participations"
        )

        df = pd.DataFrame(
            participations
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    #################################################
    # GOUVERNANCE
    #################################################

    st.header("🏛 Gouvernance")

    st.write(
        f"**Date du comité :** {gouvernance.get('date_reunion_comite_surveillance','N/A')}"
    )

    st.write(
        f"**Heure :** {gouvernance.get('heure_reunion','N/A')}"
    )

    st.write(
        f"**Participants :** {gouvernance.get('participants','N/A')}"
    )

    st.write("**Inspection AMMC :**")

    st.info(
        gouvernance.get(
            "inspection_ammc",
            "N/A"
        )
    )

    st.write("**ESG / RSE :**")

    st.info(
        gouvernance.get(
            "demarches_sdg",
            "N/A"
        )
    )

    #################################################
    # ANNEXE
    #################################################

    with st.expander(
        "Afficher le JSON complet"
    ):

        st.json(result)
