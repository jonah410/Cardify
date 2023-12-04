import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import logo from '../logo.svg';
import new_logo from '../notecard.png';
import '../App.css';
import FileUpload from "./fileupload.js";
import {Link} from 'react-router-dom';
const Converter = () => {
    const [uploadedFile, setUploadedFile] = useState(null);
    const [flashcards, setFlashcards] = useState([]); // declare state for flashcards
    const navigate = useNavigate();

    const handleFileUpload = (file) => {
        setUploadedFile(file);
    };

    const handleConvertClick = async () => {
        if (uploadedFile && uploadedFile.type === "application/pdf") {
            const formData = new FormData();
            formData.append("file", uploadedFile);

            try {
                const response = await fetch('http://127.0.0.1:5000/upload', { // call something on  port 5000 (backend) from port 3000 (frontend)
                    method: 'POST',
                    body: formData,
                });
                if(response.ok){
                    const parsedData = await response.json();
                    setFlashcards(parsedData); // Store the flashcard data in state
                    console.log(parsedData);
                    navigate('/cards', { state: { flashcards: parsedData } }); 
                } else {
                    console.error('Server responded with non-OK status:', response.status);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        } else {
            alert('Please upload a PDF file.');
        }
    };

    // flashcard obj
    const Flashcard = ({ front, back }) => {
        return (
            <div className="flashcard">
                <div className="front">{front}</div>
                <div className="back">{back}</div>
            </div>
        );
    };

    // render the component
    return (
        <div className="App">
            <header className="App-header">
                <h1>Upload your notes below!</h1>
                <FileUpload onFileUpload={handleFileUpload}/>
                <Link to="/cards">
                    <button onClick={handleConvertClick}>Convert</button>
                </Link>
                <div className="flashcards-container">
                    {flashcards.map((card, index) => (
                        <Flashcard key={index} front={card[0]} back={card[1]} />
                    ))}
                </div>
            </header>
        </div>
    );
};

export default Converter;


