import '../index.css';

const Header = () => {
  return (
    <div className="simple-navbar">
        <div className="simple-container">
            <div className="brand">Chia's Netflix Wrapped</div>
            {/* navigation menu */}
            <nav className="nav-links">
                <a href="#all-time-stats" className="w-nav-link">All -Time Stats</a>
                <a href="#top-5" className="w-nav-link">Top 5</a>
                <a href="#day-and-night" className="w-nav-link">Day and Night</a>
                <a href="#over-the-years" className="w-nav-link">Over the Years</a>
                <a href="#versus" className="w-nav-link">Versus</a>
            </nav>
        </div>
    </div>
  );
};

export default Header;