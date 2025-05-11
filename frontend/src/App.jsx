import Header from "./components/Header.jsx";
import Hero from "./components/SectionHero.jsx";
import Intro from "./components/SectionIntro.jsx";
import Grid from "./components/StatsGrid";
import Genre from "./components/Genre";
import './index.css';
import React from "react";

function App() {
    return (
      <div className="body-wrapper">
        <Header />
        <Hero />
        <Intro />
        <Genre />
        <Grid />
      </div>
    );
  }

export default App;
