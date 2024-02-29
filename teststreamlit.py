
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from PIL import Image
import fitz
import spacy
from PyPDF2 import PdfReader
import streamlit as st
import streamlit_pdf_viewer as pdf_viewer
import os
import io

# Set page title
st.set_page_config(page_title="My HR App", page_icon=":rocket:")


# Utiliser st.markdown() avec du balisage HTML pour appliquer la police, la couleur et le style gras

# Utiliser st.markdown() avec du balisage HTML pour appliquer le style spécifique
st.markdown(
    "<p style='text-align: center; font-family: Anta, monospace; color: blue; font-weight: bold; font-size: 45px;'>THE NEW WAY TO HIRE</p>",
    unsafe_allow_html=True
)

st.markdown("<p style='text-align: right; font-family: Anta, monospace; color: blue; font-size: 15px; font-weight: bold;'>powered by HireLakeAI</p>",
    unsafe_allow_html=True)

# Titre de l'application
st.image('how-ai-is-transforming-hr-1130x628.jpg')


# Utiliser st.markdown() avec du balisage HTML pour appliquer le style spécifique
st.markdown("<h1 style='text-align: center; font-family: Anta, sans-serif; color: blue;'>WELCOME TO YOUR APP</h1>",unsafe_allow_html=True)


# Utiliser st.markdown() avec du balisage HTML pour appliquer le style spécifique
st.markdown("<p style='text-align: center; font-family: Kode Mono, monospace; color: green; font-size: 48px;'>Parser CV</p>",unsafe_allow_html=True)


# Add a logo
st.sidebar.image("futureofAI.png", use_column_width=True)

# st.text("powered by HireLakeAI")
# Créer deux colonnes
col1, col2 = st.columns(2)

# Define text variable
text = ""

# Ajouter du contenu à la colonne 1
with col1:
    st.sidebar.title("Menu")
    uploaded_file = st.sidebar.file_uploader("Téléchargez votre CV au format PDF", type="pdf")

    if uploaded_file:
        pdf_data = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            image_bytes = page.get_pixmap(alpha=False).tobytes()
            st.image(image_bytes, caption=f"Page {page_num + 1}", use_column_width=True)

# Ajouter du contenu à la colonne 2
with col2:


    # Entraînement du modèle
    nlp = spacy.load('output/model-best')

    def extract_text_from_pdf(f):
        if f is None:
            return ""

        text = ""
        reader = PdfReader(f)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

    # Téléchargement du fichier PDF
    if uploaded_file is not None:
        doc_init = extract_text_from_pdf(uploaded_file)
        text = doc_init.strip()  # Remove extra spaces
        text = ' '.join(text.split())  # Join words with a single space
        print(text)
        doc = nlp(text)
        import streamlit as st

    # Boucle sur les entités et affichage avec des couleurs différentes pour les labels et les textes, et en gras
        for ent in doc.ents:
            label_html = f"<span style='font-family:Georgia; font-size: 16px; color: blue; font-weight: bold;'>{ent.label_}</span>"
            text_html = f"<span style='font-family: Arial; font-size: 16px; color: green;'>{ent.text}</span>"
            st.markdown(f"{label_html}: {text_html}", unsafe_allow_html=True)
    else:
        ("No PDF file uploaded.")
