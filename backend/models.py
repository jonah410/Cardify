from app import db

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front_text = db.Column(db.String(200), nullable=False) # Question
    back_text = db.Column(db.String(200), nullable=False) # Answer
    
    def __init__(self, front_text, back_text):
        self.front_text = front_text
        self.back_text = back_text

    def __repr__(self):
        return f'<Flashcard {self.front_text}>'