# Language Identification using Transfer Learning

## Project Description
This project identifies the language of text using a fine-tuned XLM-RoBERTa model.

## Dataset
papluca/language-identification

- 90,000 samples
- 20 languages

## Pretrained Model
FacebookAI/xlm-roberta-base

## Fine-tuned Model
https://huggingface.co/Arzooahmed/language_identification_model

## Model Accuracy
99.55%

## Technologies
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

## Run Application
Install requirements:

pip install -r requirements.txt

Run:

streamlit run app.py
