from flask_restful import Resource, reqparse
from models import Flashcard  # Import your SQLAlchemy model

# Define your RESTful resources here
class FlashcardResource(Resource):
    def get(self, flashcard_id):
        # Retrieve a specific flashcard by ID
        flashcard = Flashcard.query.get(flashcard_id)
        if flashcard is None:
            return {'message': 'Flashcard not found'}, 404
        return {
            'id': flashcard.id,
            'front_text': flashcard.front_text,
            'back_text': flashcard.back_text
        }

    def post(self):
        # Create a new flashcard
        parser = reqparse.RequestParser()
        parser.add_argument('front_text', type=str, required=True)
        parser.add_argument('back_text', type=str, required=True)
        args = parser.parse_args()
        
        flashcard = Flashcard(
            front_text=args['front_text'],
            back_text=args['back_text']
        )
        db.session.add(flashcard)
        db.session.commit()
        
        return {'message': 'Flashcard created', 'id': flashcard.id}, 201

    def put(self, flashcard_id):
        # Update a specific flashcard by ID
        parser = reqparse.RequestParser()
        parser.add_argument('front_text', type=str, required=True)
        parser.add_argument('back_text', type=str, required=True)
        args = parser.parse_args()
        
        flashcard = Flashcard.query.get(flashcard_id)
        if flashcard is None:
            return {'message': 'Flashcard not found'}, 404

        flashcard.front_text = args['front_text']
        flashcard.back_text = args['back_text']
        db.session.commit()

        return {'message': 'Flashcard updated', 'id': flashcard.id}

    def delete(self, flashcard_id):
        # Delete a specific flashcard by ID
        flashcard = Flashcard.query.get(flashcard_id)
        if flashcard is None:
            return {'message': 'Flashcard not found'}, 404

        db.session.delete(flashcard)
        db.session.commit()
        
        return {'message': 'Flashcard deleted'}