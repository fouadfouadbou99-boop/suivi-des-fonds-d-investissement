import re


def extract_general_info(text):

    result = {
        "nom_projet": None,
        "date_reunion": None
    }

    if "kiara" in text.lower():
        result["nom_projet"] = "Projet Kiara"

    patterns = [
        r"\d{2}/\d{2}/\d{4}",
        r"\d{2}-\d{2}-\d{4}",
        r"\d{1,2}\s+\w+\s+\d{4}"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            result["date_reunion"] = match.group()
            break

    return result
