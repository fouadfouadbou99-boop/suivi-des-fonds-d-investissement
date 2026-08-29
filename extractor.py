from general import extract_general_info


def extract_governance(text):

    result = {
        "quorum_atteint": None,
        "alertes": []
    }

    texte = text.lower()

    if "quorum non atteint" in texte:
        result["quorum_atteint"] = False
        result["alertes"].append(
            "Quorum non atteint"
        )

    if "dérogation" in texte:
        result["alertes"].append(
            "Dérogation détectée"
        )

    if "risque" in texte:
        result["alertes"].append(
            "Risque mentionné"
        )

    return result


def analyze_document(document_text):

    return {
        "informations_generales":
            extract_general_info(document_text),

        "gouvernance":
            extract_governance(document_text)
    }
