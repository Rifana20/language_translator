
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Set up Streamlit page
st.set_page_config(page_title="🌐 Language Translator", layout="centered")
st.title("🌍 Language Translator Bot")
st.markdown("Translate text between languages using the **Google Translate API**.")

# Language options with readable names
language_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "German": "de",
    "Malayalam": "ml"
}

languages = list(language_map.keys())

# UI input
text = st.text_area("✏️ Enter text to translate", height=150)
source = st.selectbox("🗣️ Translate from", languages, index=0)
target = st.selectbox("🎯 Translate to", languages, index=1)

# Action button
if st.button("🔄 Translate"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    elif source == target:
        st.info("Source and target languages are the same.")
    else:
        url = "https://translation.googleapis.com/language/translate/v2"
        params = {
            "q": text,
            "source": language_map[source],
            "target": language_map[target],
            "format": "text",
            "key": api_key
        }
        try:
            res = requests.post(url, data=params)
            result = res.json()
            if "data" in result:
                translated = result["data"]["translations"][0]["translatedText"]
                st.success("✅ Translation:")
                st.write(f"**{translated}**")
            else:
                st.error(f"API Error: {result}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
