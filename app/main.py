import numpy as np
import requests
import PyPDF2

# API endpoint (this is hypothetical and may vary based on actual API details)
API_ENDPOINT = "http://localhost:3001/v1/completions"

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Path to your PDF file
pdf_path = "/Users/jonahblack/Downloads/Sample_Cover_Letter.pdf"

# Extract text from the PDF
notes = extract_text_from_pdf(pdf_path)

data = {
    "query": "Parse the following text and output relevant information in flashcard format: 1) [front], 2) [back]: " + notes
}

# print(data)

headers = {}

response = requests.post(API_ENDPOINT, json=data, headers=headers)
print(response)

# Check for a valid response
if response.status_code == 200:
    result = response.text
    print(result)
    # result_text = response.json()['choices'][0]['text']
    #  print(result_text)

else:
    print(f"Error: {response.status_code} - {response.text}")
