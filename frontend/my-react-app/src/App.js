import logo from './logo.svg';
import new_logo from './notecard.png'
import './App.css';
import Converter from "./components/converter.js";
import Flashcard from "./components/flashcard.js";

function App() {
  return (
    <div className="App">
      <div className = "Logo">
      <img src={new_logo} className="App-logo" alt="logo" />
      </div>
      <header className="App-header">
        <Converter />
        <Flashcard />
      </header>
    </div>
  );
}

export default App;
