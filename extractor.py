import json
import streamlit as st
import google.generativeai as genai

from prompts import PROMPT


def analyze_document(document_text):

    try:

        # Configuration Gemini
        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        # Modèle Gemini actuel
        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        prompt = f"""
{PROMPT}

DOCUMENT À ANALYSER :

{document_text[:30000]}
"""

        response = model.generate_content(
            prompt
        )

        response_text = response.text.strip()

        # Nettoyage éventuel des balises Markdown
        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(
            response_text
        )

    except json.JSONDecodeError:

        return {
            "erreur": "Le JSON retourné par Gemini est invalide.",
            "reponse_brute": response_text
        }

    except Exception as e:

        return {
            "erreur": str(e)
        }
