import streamlit as st
from transformers import pipeline

st.title("Language Identification 🌍")

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="Arzooahmed/language_identification_model"
    )

classifier = load_model()

text = st.text_area("Enter your text")

if st.button("Identify Language"):
    if text.strip():
        result = classifier(text)[0]
        st.success(f"Language: {result['label']}")
        st.write(f"Confidence: {result['score']:.2%}")
    else:
        st.warning("Please enter some text.")
