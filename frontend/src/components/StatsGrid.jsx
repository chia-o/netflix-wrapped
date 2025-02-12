import '../index.css';

const Grid = () => {
    return(
        <div className="section-grid">
            <div className="intro-grid relative">
                <div className="stats-grid-item">
                    <div class="stats-label">Film Buff/Series Junkie?</div>
                    <div class="stats-text">Series Junkie</div>
                </div>
                <div className="stats-grid-item">
                    <div class="stats-label">Top Genre</div>
                    <div class="stats-text">Romance</div>
                </div>
                <div className="stats-grid-item">
                    <div class="stats-label">Watching On</div>
                    <div class="stats-text">TV</div>
                </div>
                <div className="stats-grid-item">
                    <div class="stats-label">Time of Day</div>
                    <div class="stats-text">Night</div>

                </div>
            </div>
        </div>
    )
}

export default Grid;


