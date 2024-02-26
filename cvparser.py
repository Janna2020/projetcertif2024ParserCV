import sys
import spacy
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import fitz  # PyMuPDF
from PIL import Image

#############################################################################################################
#############################################################################################################
def main():
    # Définir le titre de l'application
    st.title("APPLICATION IA : RESUME DE CV")

    # Ajouter une image de fond d'écran
    # image = Image.open("5152ca4a1e39e2332416b742db3ef589.jpg")
    # st.image(image, use_column_width=True)
   
    # Définir la police de texte personnalisée
    st.markdown("""
    <style>
        /* Utilisation de la police "Comic Sans MS" */
        body {
            font-family: 'Comic Sans MS', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

    # Ajouter du contenu à l'application
if __name__ == "__main__":
    main()
#################################################################################################################
st.header("Analyse de CV")
st.text("powered by HireLakeAI")
#################################################################################################################
  # Insérer une image dans la barre latérale
st.sidebar.image("idMAUPxk1q.jpg", use_column_width=True)
def main()
    # st.header("Analyse du CV")
#################################################################################################################
   # Créer deux colonnes
    col1, col2 = st.columns(2)

    # Ajouter du contenu à la colonne 1
    with col1:
        st.sidebar.title("Menu")
        uploaded_file = st.sidebar.file_uploader("télécharger votre CV au format PDF", type="pdf")

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
        st.write("Résumé du CV")

if __name__ == "__main__":
    main()
#################################################################################################################
from PyPDF2 import PdfReader
st.title('CV Parser C.IA')
from PyPDF2 import PdfReader
nlp = spacy.load('model best')
def extract_text_from_pdf(f):
    text = ""
    #with open(pdf_path, "rb") as f:
    reader = PdfReader(f)
    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text
nlp = spacy.load('output/model best')
# Chemin vers le fichier PDF à convertir en texte
#pdf_path = "cv_data_project/10247517.pdf"
pdf_path = st.file_uploader("choose a file", ["pdf"])
doc_init = extract_text_from_pdf(pdf_path)
#st.write("----------------")
#st.write(doc)
#st.write("----------------")
# Afficher le texte extrait
# print(doc)
text = ""
for page in doc_init:
    text += str(page)
# Afficher le texte extrait
# st.write(doc)
text = text.strip()
' '.join(text.split())
st.write("###############################################")
doc = nlp(text)
print(doc)
for ent in doc.ents:
    st.write(ent.label_,":", ent.text)
#st.write(doc)
st.write("##############################################")
st.title('end of CV')