import numpy as np
import requests
import PyPDF2
import g4f
from g4f.Provider import (
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    H2o,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Ylokh,
    You,
    Yqcloud,
)

API_ENDPOINT = "http://127.0.0.1:80"
API_TOKEN = "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" # hugging face api read token

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

pdf_path = "/Users/jonahblack/Downloads/Sample_Cover_Letter.pdf"
notes = extract_text_from_pdf(pdf_path)

'''response = g4f.Completion.create(
    model = 'text-davinci-003',  # This is just an example model name; use the appropriate GPT-4 model name.
    prompt="Parse the following text and output relevant information in flashcard format: 1) [front], 2) [back]: " + notes
)'''
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.Aichat,
    messages=[{"role": "user", "content": "Hello"}],
    # stream=True,
)

print(response)

# response = requests.post(API_ENDPOINT, json=data, headers=headers)
if response.status_code == 200:
    result = response.text
    print(result)
    # result_text = response.json()['choices'][0]['text']
    #  print(result_text)

else:
    print(f"Error: {response.status_code} - {response.text}")
