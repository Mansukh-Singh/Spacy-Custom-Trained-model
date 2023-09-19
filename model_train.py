import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from json_extract import data

nlp = spacy.blank('en')
db = DocBin()

for text, annot in tqdm(data['annotations']):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot['entities']:
        span = doc.char_span(start, end, label=label, alignment_mode='contract')
        if span is None:
            print('skipping entity')
        else:
            ents.append(span)
    doc.ents = ents 
    db.add(doc)
db.to_disk("train.spacy")

