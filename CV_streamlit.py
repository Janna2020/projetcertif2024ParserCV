
import streamlit as st
import fitz  # PyMuPDF
import spacy
from spacy import displacy, Language
from spacy.lang.fr.examples import sentences
import spacy_streamlit
import fitz  # PyMuPDF


st.title("PARSER CV")
st.image('parsing-news.jpg', caption='process analyse CV', width=800)
st.image('resume-parser-and-indexerpersona.png')
st.sidebar.title("sommaire")
st.sidebar.markdown("1er partie : eufzeiufhzehf"
                    )
st.sidebar.markdown("2ème partie : fbefbzebfzeb"
                    )

# conversion du PDF en texte
def pdf_to_text(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
    return text

# lecteur du texte
pdf_text=pdf_to_text("CV ingenieur informatique DATA.pdf")


# lecture du texte sur streamlit
# st.write(pdf_text)

models = ["en_core_web_sm", "en_core_web_md"]
default_text = pdf_text
spacy_streamlit.visualize(models, default_text)


from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
pattern = [{"TEXT": "DATA"}]
matcher.add("MarketingPattern", [pattern])
doc = nlp(pdf_text)
st.write(matcher(doc))

match = matcher(doc)
match_id, start, end = match[0]
st.write(doc[start:end])

