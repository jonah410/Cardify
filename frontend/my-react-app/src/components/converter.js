import logo from '../logo.svg';
import new_logo from '../notecard.png'
import '../App.css';
const converter = () => {
    return (
        <div className = "App">
            <header className="App-header">
                <h1>Upload your notes below!</h1>
                    
                    <button>Convert</button>
                    <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                    >
                    Learn React
                    </a>
            </header>
        </div>
    )
}
export default converter;