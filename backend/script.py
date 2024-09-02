import requests
import tempfile
import fitz
import re
from config import Config
import openai

# initialize OpenAI client API
client = openai.OpenAI(
    api_key=Config.AI_API_KEY,
    base_url="https://api.aimlapi.com"
)

# request pdf text from link
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

pdf_document.close()

# clean full_text
full_text = full_text.replace("-\n", "").replace("\n", " ")
full_text = re.sub(r'\s+', ' ', full_text).strip()

# new line after "Continued on Page"
full_text = re.sub(r'(Continued on Page [A-Z]\d+)', r'\1\n\n\n', full_text)

# split text into paragraphs
paragraphs = full_text.split('\n\n')  

# Author Scraping ------------------------------------------------------------------------
# retrieve last lines for author names
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

# Possible name for author regex pattern
pattern = r'^(.*?)(?: By (.+?) Continued on Page [A-Z]\d+| By (.+))$'
matches = [re.match(pattern, line) for line in filtered_last_lines]

final_authors = []
# Extract authors
for match in matches:
    if match:
        # headline = match.group(1).strip()
        authors = match.group(2).strip() if match.group(2) else match.group(3).strip()
        author_list = authors.split()
        
        for word in author_list:
            # condition:
                final_authors.append(word)
        
        verifiedAuthors = ' '.join(final_authors)

final_authors_str = ' '.join(final_authors)
print(final_authors_str)

system_content = ""
user_content = f"What are the full names in this list: {final_authors_str}"

chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=128,
)

response = chat_completion.choices[0].message.content
print("AI/ML API:\n", response)
