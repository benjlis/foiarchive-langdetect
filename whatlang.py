import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

@Language.factory("language_detector")
def create_language_detector(nlp, name):
    return LanguageDetector(language_detection_function=None)

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe('language_detector')
# text = 'This is an english text.'
text = """
Plus de cent ans apres leur renaissance moderne, les Jeux olympiques retourneront en
aout 2004 a Athenes, «berceau de la civilisation et de la democratie». Aujourd'hui
encore, les Jeux demeurent une competition prestigieuse et unique, puisqu'ils
contribuent a promouvoir, a travers tous les continents, I'echange, la fraternite et la
solidarite entre les peuples : des valeurs essentielles q
"""

doc = nlp(text)
# document level language detection. Think of it like average language of the document!
print(doc._.language)
# sentence level language detection
# for sent in doc.sents:
#    print(sent, sent._.language)
