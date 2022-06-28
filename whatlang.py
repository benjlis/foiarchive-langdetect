import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
import psycopg2
import aiosql
import csv


@Language.factory("language_detector")
def create_language_detector(nlp, name):
    return LanguageDetector(language_detection_function=None)


# spaCy initialization
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('language_detector')

# db-related configuration
conn = psycopg2.connect("")
stmts = aiosql.from_path("whatlang.sql", "psycopg2")

langlist = []
for index, data in enumerate(stmts.get_doc_bodies(conn=conn)):
    id, body = data
    doc = nlp(body)
    r = (id, doc._.language['language'], doc._.language['score'])
    print(index, r)
    langlist.append(r)

outfile = "whatlang.csv"
fields = ['id', 'language', 'score']
with open(outfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(langlist)
