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
def extract_votes(text):

    votes = []

    texte = text.lower()

    keywords = [
        "approuvé",
        "rejeté",
        "abstention",
        "vote"
    ]

    for mot in keywords:

        if mot in texte:

            votes.append(mot)

    return votes
    def extract_risks(text):

    risques = []

    mots = [
        "risque",
        "litige",
        "contentieux",
        "défaut",
        "retard",
        "impayé",
        "perte"
    ]

    texte = text.lower()

    for mot in mots:

        if mot in texte:

            risques.append(mot)

    return list(set(risques))
