STEP 1
# Define base_config.cfg in your directory and then run this command
# !python -m spacy init fill-config base_config.cfg config.cfg

STEP 2
# !python -m spacy init config config.cfg --lang en --pipeline ner --optimize efficiency --force

Step 3
# !python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy

Website for tagging
# https://tecoholic.github.io/ner-annotator/