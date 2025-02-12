import Header from "./components/Header.jsx";
import Hero from "./components/SectionHero.jsx";
import Intro from "./components/SectionIntro.jsx";
import Grid from "./components/StatsGrid";
import './index.css';

function App() {
    return (
      <div className="body-wrapper">
        <Header />
        <Hero />
        <Intro />
        <Grid />
      </div>
    );
  }

export default App;
