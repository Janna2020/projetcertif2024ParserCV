import spacy
from PyPDF2 import PdfReader
import streamlit as st
import streamlit_pdf_viewer as pdf_viewer
import os

# entrainement du modèle
nlp = spacy.load('output/model-best')

# Titre de l'application
st.header("Analyse de CV")
st.text("powered by HireLakeAI")

# conversion du modèle pdf en txt
#def extract_text_from_pdf(f):
#   text = ""
#   #with open(pdf_path, "rb") as f:
#   reader = PdfReader(f)
 #   num_pages = len(reader.pages)
  #  for page_num in range(num_pages):
  #      page = reader.pages[page_num]
   #     text += page.extract_text()
    #return text

# téléchargement du fichier PDF
# pdf_path = st.file_uploader("choose a file", ["pdf"])
# doc_init = extract_text_from_pdf(pdf_path)





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
pdf_file = st.file_uploader("Choose a file", ["pdf"])
if pdf_file is not None:
    doc_init = extract_text_from_pdf(pdf_file)
    text = doc_init.strip()  # Remove extra spaces
    text = ' '.join(text.split())  # Join words with a single space
    print(text)
    doc = nlp(text)
    for ent in doc.ents:
        st.write(ent.label_, ":", ent.text)
else:
    ("No PDF file uploaded.")



# st.write("----------------")
# st.write(doc_init)
# st.write("----------------")
# Afficher le texte extrait
# print(doc)


# conversion en str
#   text = ""
# for page in doc_init:
#   text += str(page)

# suppression des espaces
# text = text.strip()
# ' '.join(text.split())

#st.write("###############################################")
#doc = nlp(text)
#for ent in doc.ents:
    #st.write(ent.label_,":", ent.text)
#st.write("##############################################")
st.title('resume  of CV') 


# transformation du CV en résumé
# doc = nlp(text)

# génération du résumé
#for ent in doc.ents:
    #print(ent.label_,":", ent.text)