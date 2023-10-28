import g4f
# from g4f.api import run_api
import PyPDF2
import re

# run_api()
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

def parse_text(response):
    # Split the input string into entries based on newline character
    entries = response.strip().split('\n')
    result = []
    
    for text in entries:
        # Split the text based on ":"
        split_text = re.split(r' : ', text)
        # Filter out empty strings and unwanted parts
        split_text = [item for item in split_text if (item) and not item.endswith('.')]
        
        # Check if the length is as expected (should be 2 after splitting)
        if len(split_text) == 2:
            result.append(split_text)
        else:
            print("Error in parsing: ", text)
            
    # Transpose the result to get the required 2xn array
    transposed_result = [list(x) for x in zip(*result)]
    return transposed_result

# Path to your PDF file
pdf_path = "/Users/jonahblack/Downloads/08_22 - lecture 1 notes.pdf"

# Extract text from the PDF
notes = extract_text_from_pdf(pdf_path)

query = "Parse the following text and output relevant information in flashcard format: 1) [front], 2) [back]: " + notes # for example, if the input is [input], you should output [desired output]

# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": query}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

print(response)

# something is wrong here - what else is needed to parse the stream?
'''response_content = ''
for message in response:
    if 'content' in message['data']:
        response_content += message['data']['content']

arr = parse_text(response_content)
print(arr)'''



# next step: return the response as a string (put top and bottom into a 2xn array), parse the response, set the text into the appropriate parameter for the flashcard datatype

# maybe use check for a valid response as well 
''' if response.status_code == 200:
    result = response.text
    print(result)
    # result_text = response.json()['choices'][0]['text']
    #  print(result_text)

else:
    print(f"Error: {response.status_code} - {response.text}") '''

# diff this with the current response structure
''' # normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Hello"}],
)  # alternative model setting '''