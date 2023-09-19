import spacy 
from spacy import displacy

nlp1 = spacy.load("output\model-best")

doc = nlp1("is it possible to get maths lesson for 4th grade student having duration less than 2 hr and it must have rating graeter than 4")

# displacy.serve(doc, style="ent")
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")