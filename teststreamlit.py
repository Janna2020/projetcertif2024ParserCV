
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from PIL import Image
import fitz
import spacy
from PyPDF2 import PdfReader
import streamlit as st
import streamlit_pdf_viewer as pdf_viewer
import os


# Set page title
st.set_page_config(page_title="My HR App", page_icon=":rocket:")

# Add a title and description
st.title("Welcome to My HR App!")

# Add a logo
st.sidebar.image("logoHireAI.avif", use_column_width=True)

# Add an image from a URL
st.image("imageappliIAIHR.jpeg", caption="AI application for Human Ressources", use_column_width=True)




st.title("Analyse de CV")
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
    # Contenu de la colonne 2
    st.title("PARSER CV")

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
        for ent in doc.ents:
            st.write(ent.label_, ":", ent.text)
    else:
        st.write("No PDF file uploaded.")
