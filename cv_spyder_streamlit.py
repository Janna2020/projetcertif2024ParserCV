import spacy
import pickle
import random
import sys, fitz


train_data = pickle.load(open('train_data.pkl', 'rb'))
print(train_data[0])

import spacy
import random
import pickle

train_data = pickle.load(open('train_data.pkl', 'rb'))
print(train_data[0])

nlp = spacy.blank('en')

# Check if 'ner' is in the pipe_names
if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe('ner')
else:
    ner = nlp.get_pipe('ner')  # Get the existing 'ner' component

# Add labels to the NER component
for _, annotation in train_data:
    for ent in annotation['entities']:
        ner.add_label(ent[2])

# Disable all other pipes and train only NER
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()

    for itn in range(10):
        print("Starting iteration " + str(itn))
        random.shuffle(train_data)
        losses = {}

        for text, annotations in train_data:
            try:
                nlp.update(
                    [text],          # batch of texts
                    [annotations],   # batch of annotations
                    drop=0.2,        # dropout - make it harder to memorize data
                    losses=losses,
                )
            except Exception as e:
                pass

        print(losses)

nlp.to_disk('nlp_model')

nlp_model = spacy.load('nlp_model')

train_data[0][0]

doc = nlp_model(train_data[0][0])
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}}- {ent.text}')

test = spacy.load("en_core_web_sm")
for ent in test("Apple is looking at buying U.K. startup for $1 billion").ents:
  print(f'{ent.label_.upper():{10}} - {ent.text}')

#import random
#import sys, fitz
#fname = 'CV ingenieur informatique DATA.pdf'
#@doc = fitz.open(fname)
#text=''
#for page in doc:
    #text = text + str(page.get_text())

#tx = " ".join(text.split('\n'))
#print(tx)
