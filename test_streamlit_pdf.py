import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import fitz  # PyMuPDF
from PIL import Image

###################################################################################

########################################################
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


st.header("Analyse de CV")
st.text("powered by HireLakeAI")

   # Insérer une image dans la barre latérale
st.sidebar.image("idMAUPxk1q.jpg", use_column_width=True)
def main():
    # st.header("Analyse du CV")


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








