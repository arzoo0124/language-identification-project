
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Language Identification",
    page_icon="🌍"
)

st.title("Language Identification 🌍")
st.write("Enter text to identify its language.")

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="Arzooahmed/language_identification_model"
    )

classifier = load_model()

language_names = {
    "fr": "French",
    "es": "Spanish",
    "en": "English",
    "ur": "Urdu",
    "ar": "Arabic",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "hi": "Hindi",
    "nl": "Dutch",
    "tr": "Turkish",
    "sv": "Swedish",
    "pl": "Polish",
    "th": "Thai",
    "el": "Greek",
    "bg": "Bulgarian"
}

text = st.text_area("Enter your text here:")

if st.button("Identify Language"):
    if text.strip():
        result = classifier(text)[0]
        code = result["label"]
        language = language_names.get(code, code)

        st.success(f"Language: {language}")
        st.write(f"Confidence: {result['score']:.2%}")
    else:
        st.warning("Please enter some text.")
