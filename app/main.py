import g4f
import PyPDF2

g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider

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

query = "Parse the following text and output relevant information in flashcard format: 1) [front], 2) [back]: " + notes

# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": query}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

''' # normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Hello"}],
)  # alternative model setting '''

print(response)

# next step: return the response as a string, parse the response, set the text into the appropriate parameter for the flashcard datatype

# maybe use check for a valid response as well 
''' if response.status_code == 200:
    result = response.text
    print(result)
    # result_text = response.json()['choices'][0]['text']
    #  print(result_text)

else:
    print(f"Error: {response.status_code} - {response.text}") '''