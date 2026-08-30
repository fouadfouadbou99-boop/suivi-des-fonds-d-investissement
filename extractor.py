import json
import streamlit as st
import google.generativeai as genai

from prompts import PROMPT


def analyze_document(document_text):

    response_text = ""

    try:

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        model = genai.GenerativeModel(
            "models/gemini-3.6-flash"
        )

        prompt = f"""
{PROMPT}

DOCUMENT A ANALYSER :

{document_text[:30000]}
"""

        response = model.generate_content(
            prompt
        )

        response_text = response.text

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
            "erreur": "JSON invalide retourné par Gemini",
            "reponse_brute": response_text
        }

    except Exception as e:

        return {
            "erreur": str(e)
        }
