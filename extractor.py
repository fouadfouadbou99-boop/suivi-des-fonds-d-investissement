from general import extract_general_info
from gouvernance import extract_governance


def analyze_document(document_text):

    result = {}

    result["informations_generales"] = (
        extract_general_info(document_text)
    )

    result["gouvernance"] = (
        extract_governance(document_text)
    )

    return result
