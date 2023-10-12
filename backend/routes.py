from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Flashcard
from app.forms import UploadForm  # If you use Flask-WTF for forms

@app.route('/')
def index():
    flashcards = Flashcard.query.all()
    return render_template('flashcards.html', flashcards=flashcards)

@app.route('/upload', methods=['POST'])
def upload_file():
    form = UploadForm(request.form)  # If you use Flask-WTF for forms
    if form.validate_on_submit():
        uploaded_file = request.files['file']
        if uploaded_file:
            # Process the uploaded PDF and generate flashcards
            # Save flashcards to the database
            flash('Flashcards generated successfully', 'success')
            return redirect(url_for('index'))
    flash('File upload failed', 'danger')
    return redirect(url_for('index'))

@app.route('/flashcards')
def view_flashcards():
    flashcards = Flashcard.query.all()
    return render_template('flashcards.html', flashcards=flashcards)
