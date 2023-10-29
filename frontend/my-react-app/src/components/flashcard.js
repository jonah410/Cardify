import '../App.css';
import ReactFlipCard from 'reactjs-flip-card'

const styles = {
    card: {
        background: 'rgb(0, 179, 173)',
        color: 'white',
        borderRadius: '20px',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        // height: '100%',
        // width: '100%'
    },
    allcard: {
        width: '100%',
        height: '100%'
    }
};

const flashcard = () => {
    return (
        <div style={{height:'200px', width: '30%'}}>
                <ReactFlipCard
                    containerStyle={styles.allcard}
                    frontStyle={styles.card}
                    backStyle={styles.card}
                    frontComponent={<div>Word/ Big Idea/ Frontside</div>}
                    backComponent={<div>Definition/ Significance/ Backside</div>}
                />
        </div>
    )
}
export default flashcard;