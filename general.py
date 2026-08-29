import re


def extract_general_info(text):

    result = {
        "nom_projet": None,
        "date_reunion": None
    }

    if "kiara" in text.lower():

        result["nom_projet"] = "Projet Kiara"

    date_match = re.search(
        r"\d{2}/\d{2}/\d{4}",
        text
    )

    if date_match:

        result["date_reunion"] = (
            date_match.group()
        )

    return result
