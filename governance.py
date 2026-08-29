import re


def extract_participants(text):

    participants = []

    patterns = [
        "CMR",
        "Attijari",
        "CDG",
        "CFG",
        "Valoris"
    ]

    for p in patterns:

        if p.lower() in text.lower():

            participants.append(p)

    return participants
