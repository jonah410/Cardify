import logo from '../logo.svg';
import new_logo from '../notecard.png'
import '../App.css';
import FileUpload from "./fileupload.js";
const converter = () => {
    return (
        <div className = "App">
            <header className="App-header">
                <h1>Upload your notes below!</h1>
                    <FileUpload/>
                    <button>Convert</button>
            </header>
        </div>
    )
}
export default converter;