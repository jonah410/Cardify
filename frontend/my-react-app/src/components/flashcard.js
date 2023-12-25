import React from 'react';
import ReactFlipCard from 'reactjs-flip-card';

const styles = {
    card: {
        background: 'rgb(0, 179, 173)',
        color: 'white',
        borderRadius: '20px',
        display: 'flex',
        flexDirection: 'column', // ensures content is laid out in a single column
        justifyContent: 'center',
        alignItems: 'center',
        padding: '20px', // adds padding inside the card
        overflow: 'auto', // adds scrolling to the card if the content is too long
        fontSize: '16px', // adjust font size as needed
        textAlign: 'center', // centers text horizontally
        wordWrap: 'break-word', // ensures that long words don't overflow
        height: '100%', // makes sure the card fills the container
    },
    allcard: {
        width: '100%',
        height: '100%',
    },
};


const Flashcard = ({ front, back }) => {
    return (
        <div style={{height:'200px', width: '30%', margin: '10px'}}>
            <ReactFlipCard
                containerStyle={styles.allcard}
                frontStyle={styles.card}
                backStyle={styles.card}
                frontComponent={<div style={{ height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>{front}</div>}
                backComponent={<div style={{ height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>{back}</div>}
            />
        </div>
    );
};

export default Flashcard;
