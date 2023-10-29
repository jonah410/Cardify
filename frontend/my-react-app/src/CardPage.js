import Flashcard from "./components/flashcard.js";
import './App.css';
import new_logo from './notecard.png'


function CardPage() {
  return (
    <div className="App">
        <h1>Your Flashcards:</h1>
      {/* <div className = "Logo">
      <img src={new_logo} className="App-logo" alt="logo" />
      </div> */}
      <header className="Card-page-header">
            <Flashcard />
            <Flashcard />
            <Flashcard />
            <Flashcard />
      </header>
    </div>
  );
}

export default CardPage;
