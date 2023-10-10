from flask import Flask
from flask_restful import Api, Resource # API to interact with front-end
from flask_cors import CORS # To allow cross-origin requests from frontend to backend
from flask_sqlalchemy import SQLAlchemy # To allow for us to use SQLite as our database

app = Flask(__name__)

@app.route('/') # This will tell the program to default to the home page
def cardify_home():
    return 'Welcome to <h1>Cardify\'s<h1> main page. If this is shown, there is no error with the rest api or the sqlite database.'

if __name__ == '__main__':
    app.run(debug=True)


# Creating an API object:
api = Api(app)
# NOTE: WE STILL NEED TO CREATE RESOURCES, ADD THE RESOURCES TO THE API, DEFINE URL ROUTES, ETC.


# Configuring the Database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardify_database.db'  # Replace with your desired database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# NOTE: WE STILL NEED TO DEFINE A DATABASE MODEL, CREATE DATABASE TABLES, ETC. --> Closing database connections as well?