import '../index.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const Genre = () => {
  const [genre, setGenre] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/data/top-genre/')
      .then(response => {
        setGenre(response.data.genre); // or response.data.genre if needed
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching top genre:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  return <div style={{ color: 'red', fontSize: '20px' }}>Top Genre: {genre}</div>;
};

/*
const Genre = () => {
    // by default, genre will be null before fetching data
    const [genre, setGenre] = useState(null);
    const [loading, setLoading] = useState(true);
    
    // fetch data via API
    useEffect(() => {
      axios.get('http://127.0.0.1:8000/data/top-genre/')
        .then(res => {
            setGenre(response.data.genre); 
            setLoading(false);
        })
        .catch(err => {
            console.error("Error fetching genre:", err);
            setLoading(false);
        });
    }, []);
  
    // return data
    if (loading) return <p>Loading...</p>;
    
    //return <div style={{ color: 'red', fontSize: '20px' }}>Top Genre: {genre}</div>;
    return <div className='intro-text'>
        Top Genre: {top_genre}
        </div>;
    
};
*/

export default Genre;