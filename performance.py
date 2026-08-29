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
