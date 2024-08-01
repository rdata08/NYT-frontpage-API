import requests
import tempfile
import fitz

url = 'https://static01.nyt.com/images/2024/07/29/nytfrontpage/scan.pdf'
response = requests.get(url)

with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
    temp_file.write(response.content)
    temp_pdf_path = temp_file.name

pdf_document = fitz.open(temp_pdf_path)

full_text = ""
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    full_text += page.get_text()

print(full_text)

pdf_document.close()
