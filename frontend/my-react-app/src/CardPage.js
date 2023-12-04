import React from 'react';
import { useLocation } from 'react-router-dom';
import Flashcard from "./components/flashcard.js";

function CardPage() {
  const location = useLocation();
  const flashcards = location.state?.flashcards || []; // Get flashcards from route state
  console.log('Flashcards:', flashcards); // Check the flashcards data


  return (
    <div className="App">
        <h1>Your Flashcards:</h1>
        <header className="Card-page-header">
          {flashcards.map((card, index) => (
            <Flashcard key={index} front={card[0]} back={card[1]} />
          ))}
        </header>
    </div>
  );
}

export default CardPage;
