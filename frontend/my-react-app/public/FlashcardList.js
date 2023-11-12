// FlashcardList.js

import React, { useState, useEffect } from 'react';

function FlashcardList() {
    const [flashcards, setFlashcards] = useState([]);

    useEffect(() => {
        fetch('/api/flashcards')
            .then(response => response.json())
            .then(data => setFlashcards(data.flashcards))
            .catch(error => console.error('Error fetching flashcards:', error));
    }, []); // Empty array means so that it only runs once after the first render

    return (
        <div>
            <h2>Flashcards</h2>
            <ul>
                {flashcards.map(card => (
                    <li key={card.id}>
                        <strong>Question:</strong> {card.question}<br />
                        <strong>Answer:</strong> {card.answer}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default FlashcardList;