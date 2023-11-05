from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration settings
app.config.from_object('config.Config')

db = SQLAlchemy(app)
api = Api(app)

from resources import FlashcardResource
api.add_resource(FlashcardResource, '/flashcards/<int:flashcard_id>')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']

        if pdf_file:
            # Ensure the uploaded file is a PDF
            if pdf_file.filename.endswith('.pdf'):

                pdf_filename = secure_filename(pdf_file.filename)
                upload_dir = 'uploads'
                # Create the upload directory if it doesn't exist
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)
                # Save the PDF file to the upload directory
                pdf_path = os.path.join(upload_dir, pdf_filename)
                pdf_file.save(pdf_path)

                # Redirect to the pdf processing page
                return redirect(url_for('upload'))

    return render_template('home.html', title='Home Page')


@app.route('/upload', methods=['POST'])
def upload_pdf():
    pdf_file = request.files['pdf_file']

    if pdf_file:
        try:
            # Save the uploaded PDF to a directory
            pdf_file.save('path_to_upload_directory/' + pdf_file.filename)

            # Implement Jonah's OpenAI API call here

            # Create a flashcard and store it in the database
            new_flashcard = Flashcard(
                question='Your question here',
                answer='Your answer here'
            )
            db.session.add(new_flashcard)
            db.session.commit()

            # Return a success response
            return jsonify({'message': 'PDF uploaded successfully', 'filename': pdf_file.filename})
        except Exception as e:
            # Handle any errors that may occur during the file saving process
            return jsonify({'error': str(e)}), 500
    else:
        # Handle the case where no file was uploaded
        return jsonify({'message': 'No file uploaded'}), 400
    
    
# Route for the flashcard listing page
@app.route('/flashcards', methods=['GET'])
def flashcard_listing():
    # Query the database to retrieve flashcards
    flashcards = Flashcard.query.all()
    return render_template('flashcard_listing.html', title='Flashcards', flashcards=flashcards)

# Route for editing flashcards page
@app.route('/edit_flashcard/<int:flashcard_id>', methods=['GET', 'POST'])
def edit_flashcard(flashcard_id):
    flashcard = Flashcard.query.get(flashcard_id)

    if request.method == 'POST':
        flashcard.question = request.form['question']
        flashcard.answer = request.form['answer']
        db.session.commit()
        return redirect(url_for('flashcard_listing'))

    return render_template('edit_flashcard.html', flashcard=flashcard)

if __name__ == '__main__':
    app.run(debug=True)