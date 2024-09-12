import sqlite3
from docx import Document

test = Document('test.docx')

con = sqlite3.connect('tests.sqlite')

cur = con.cursor()


