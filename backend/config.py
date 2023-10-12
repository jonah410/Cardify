import os

# store configuration variables

class Config:
    # secret key for security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for memory efficiency

    # file upload settings
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'pdf'}  # only allowed file extensions

    # API keys and secrets
    EXTERNAL_GPT_API_KEY = os.environ.get('EXTERNAL_API_KEY') # FIX THIS LATER WITH OPEN AI API KEY

    DEBUG = True
    TESTING = False