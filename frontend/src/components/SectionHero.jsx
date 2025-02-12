/*
import '../index.css';

const Hero = () => {
    return (
        <div className="container">
            <div className="hero-image">
                <img src="/images/Paper 3 (open)(1).png" alt="main image" className="image-absolute"></img>
                <img src="/images/Untitled design(2).png" alt="accent image" className="image-absolute-accent"></img>
            </div>
        </div>
    )
};

export default Hero;
*/

import React from 'react';
import '../index.css';

const Hero = () => {
  return (
    <div className="section-hero">
        <div className="container">
            <img src="/images/Paper 3 (open)(1).png" alt="Main Image" className="image-absolute"/>
            <img src="/images/Untitled design(2).png" alt="Accent Image" className="image-absolute-accent"/>
        </div>
    </div>
  );
};

export default Hero;
