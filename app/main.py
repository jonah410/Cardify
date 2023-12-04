from flask import Flask, request, jsonify
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

def parse_text(response): # IF THIS RETURNS AN EMPTY ARRAY, REGENERATE THE RESPONSE AND RUN IT AGAIN
    # Split the input string into entries based on "Front:" and "Back:"
    front_entries = re.split(r'Front: ', response.strip())
    result = []
    
    for entry in front_entries[1:]:  # Skip the first split as it will be empty
        # Further split each entry into front and back using "Back:"
        parts = re.split(r'Back: ', entry)
        if len(parts) == 2:
            front = parts[0].strip()
            back = parts[1].strip()
            # Ensure we do not include the number in the front text
            front = re.sub(r'^\d+\.\s*', '', front)
            result.append([front, back])
        else:
            print("Error in parsing: ", entry)
            
    return result

def generate_response(query):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        stream=True,
    )

    complete_message = ''
    for char in response:
        if isinstance(char, str):  # Check if the response item is a string
            complete_message += char

    return complete_message


# Path to your PDF file
pdf_path = "/Users/jonahblack/Downloads/08_22 - lecture 1 notes.pdf"

# Extract text from the PDF
notes = extract_text_from_pdf(pdf_path)

query = "Parse the following text and output relevant information in flashcard format: 1: [front], 2: [back] " + notes # for example, if the input is [input], you should output [desired output]

max_attempts = 5  # Set a maximum number of attempts to avoid infinite looping
attempt = 0
parsed_data = []

while len(parsed_data) == 0 and attempt < max_attempts:
    complete_message = generate_response(query)
    parsed_data = parse_text(complete_message)
    attempt += 1

if len(parsed_data) == 0:
    print("Failed to generate valid data after multiple attempts.")
else:
    print(parsed_data)
    
# print(complete_message)
# parsed_data = parse_text(complete_message) # to implement: if parsed_data.size() == 0, rerun  the query (until it generates with the thing we want to split on)
# print(parsed_data)

# next step: return the response as a string (put top and bottom into a 2xn array) - DONE, parse the response - DONE, set the text into the appropriate parameter for the flashcard datatype

# maybe use this check for a valid response as well 
''' if response.status_code == 200:
    result = response.text
    print(result)
    # result_text = response.json()['choices'][0]['text']
    #  print(result_text)

else:
    print(f"Error: {response.status_code} - {response.text}") '''
