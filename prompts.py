PROMPT = """
Tu es un analyste senior spécialisé dans les fonds de Private Equity, OPCC, OPCI et Asset Management.

Analyse intégralement le document et retourne uniquement un JSON valide.

Structure attendue :

{
  "informations_generales": {
    "nom_du_fonds": "",
    "forme_juridique": "",
    "nature_des_investissements": "",
    "date_de_constitution": "",
    "date_second_closing": "",
    "taille_second_closing": "",
    "taille_totale_du_fonds": "",
    "total_des_liberations_au_31_12_2025": "",
    "part_liberee_cmr": "",
    "duree_du_fonds": "",
    "actionnariat": {}
  },

  "performance": {
    "total_investi_dh": null,
    "valorisation_portefeuille_dh": null,
    "plus_value_totale_dh": null,
    "tri": "",
    "valeur_liquidative_initiale_dh": null,
    "valeur_liquidative_actuelle_dh": null,
    "progression_valeur_liquidative": ""
  },

  "investissements": [],

  "desinvestissements": [],

  "participations": [],

  "gouvernance": {
    "date_reunion_comite_surveillance": "",
    "heure_reunion": "",
    "participants": "",
    "inspection_ammc": "",
    "demarches_sdg": ""
  },

  "risques": [],

  "alertes": [],

  "actions_a_mener": [],

  "decisions": [],

  "opci": null,

  "synthese_executive": ""
}

Consignes :

- Retourner exclusivement du JSON.
- Aucune phrase avant ou après le JSON.
- Extraire tous les montants, pourcentages et indicateurs disponibles.
- Identifier les participations.
- Identifier les risques.
- Identifier les alertes.
- Identifier les décisions.
- Identifier les actions à mener.
- Produire une synthèse exécutive de 10 à 15 lignes maximum destinée à un investisseur institutionnel (CMR).
- Utiliser null lorsqu'une information n'est pas trouvée.
"""
