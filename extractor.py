import json, streamlit as st, google.generativeai as genai
from ai.prompts import PROMPT

def analyze_document(document_text):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("models/gemini-3.6-flash")
        prompt=f"{PROMPT}

DOCUMENT:
{document_text[:2000]}"
        r=model.generate_content(prompt)
        txt=r.text.replace('```json','').replace('```','').strip()
        return json.loads(txt)
    except Exception as e:
        return {'erreur':str(e)}
