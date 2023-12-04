import React from 'react';
import ReactFlipCard from 'reactjs-flip-card';

const styles = {
    card: {
        background: 'rgb(0, 179, 173)',
        color: 'white',
        borderRadius: '20px',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
    },
    allcard: {
        width: '100%',
        height: '100%',
    }
};

const Flashcard = ({ front, back }) => {
    return (
        <div style={{height:'200px', width: '30%'}}>
            <ReactFlipCard
                containerStyle={styles.allcard}
                frontStyle={styles.card}
                backStyle={styles.card}
                frontComponent={<div>{front}</div>}
                backComponent={<div>{back}</div>}
            />
        </div>
    );
};

export default Flashcard;
