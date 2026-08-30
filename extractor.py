import json
import streamlit as st
import google.generativeai as genai

from prompts import PROMPT


def analyze_document(document_text):

    try:

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        model = genai.GenerativeModel(
            "gemini-1.5-pro"
        )

        prompt = f"""
{PROMPT}

DOCUMENT :

{document_text[:25000]}
"""

        response = model.generate_content(
            prompt
        )

        response_text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(
            response_text
        )

    except Exception as e:

        return {
            "erreur": str(e)
        }
