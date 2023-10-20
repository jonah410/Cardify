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

                # Implement PDF processing logic here:

                # Redirect to the flashcard listing page
                return redirect(url_for('flashcard_listing'))

    return render_template('home.html', title='Home Page')
    
# Route for the flashcard listing page
@app.route('/flashcards', methods=['GET'])
def flashcard_listing():
    # Query the database to retrieve flashcards
    flashcards = Flashcard.query.all()
    return render_template('flashcard_listing.html', title='Flashcards', flashcards=flashcards)

if __name__ == '__main__':
    app.run(debug=True)