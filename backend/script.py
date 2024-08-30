import requests
import tempfile
import fitz
import re
from backend.config import Config
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key= Config.db_openaiapikey
)

print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)

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

pdf_document.close()

full_text = full_text.replace("-\n", "").replace("\n", " ")
full_text = re.sub(r'\s+', ' ', full_text).strip()

# new line after "Continued on Page"
full_text = re.sub(r'(Continued on Page [A-Z]\d+)', r'\1\n\n\n', full_text)

print()
print()
paragraphs = full_text.split('\n\n')
last_lines = []
for paragraph in paragraphs:
    lines = paragraph.split('. ')
    if lines:
        last_line = lines[-1]
        last_lines.append(last_line)

filtered_last_lines = []
for last_line in last_lines:
    if len(last_line.split()) >= 5:
        filtered_last_lines.append(last_line)
        # print(last_line)

print()
print()
pattern = r'^(.*?)(?: By (.+?) Continued on Page [A-Z]\d+| By (.+))$'

matches = [re.match(pattern, line) for line in filtered_last_lines]

# Print extracted headlines and authors
for match in matches:
    if match:
        headline = match.group(1).strip()
        authors = match.group(2).strip() if match.group(2) else match.group(3).strip()

        author_list = authors.split()
        final_authors = []
        for word in author_list:
            # condition:
                final_authors.append(word)
        
        print(final_authors)
        verifiedAuthors = ' '.join(final_authors)

        # print(f"Headline: {headline}")
        # print(f"Authors: {verifiedAuthors}")
        print()

# pattern = r'\b[A-Z][A-Za-z\s]+(?:[A-Z][a-z]+)?\sBy\s[A-Z][A-Z]+\s(?:and\s[A-Z][A-Z]+)?'
# matches = re.findall(pattern, full_text)
# for match in matches:
#     print(match)