import requests
import tempfile
import fitz
import pycountry

url = 'https://static01.nyt.com/images/2024/07/29/nytfrontpage/scan.pdf'
response = requests.get(url)

countries = set()
tags = set()
authors = set()
headlines = set()

with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
    temp_file.write(response.content)
    temp_pdf_path = temp_file.name

pdf_document = fitz.open(temp_pdf_path)

full_text = ""
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    full_text += page.get_text()

full_text_split = full_text.split()
for i, word in range(len(full_text_split)):
    if word == "By" or word == "by":
        authors.add(full_text_split[i+1])
        

for word in full_text[:100].split():
    if word in pycountry.countries:
        countries.add(word)
    

print(full_text)

pdf_document.close()
