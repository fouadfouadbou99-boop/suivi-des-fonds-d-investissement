import re


def extract_performance(text):

    result = {
        "TRI": None,
        "TVPI": None,
        "DPI": None,
        "RVPI": None
    }

    metrics = ["TRI", "TVPI", "DPI", "RVPI"]

    for metric in metrics:

        pattern = rf"{metric}\\s*[:=]?\\s*([\\d\\.,]+)"

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            result[metric] = match.group(1)

    return result
def detect_opci(text):

    mots = [
        "opci",
        "immeuble",
        "locataire",
        "taux d'occupation",
        "valeur locative"
    ]

    score = 0

    texte = text.lower()

    for mot in mots:

        if mot in texte:

            score += 1

    return score >= 2
