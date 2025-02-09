# netflix-wrapped
A project that creates a Spotify Wrapped dupe for my Netflix viewing history from 2012 - 2025. 

I wrote the app in Python and used a Postgres backend to store the viewing data. I used the OMDB API to fecth genres for the titles and read a JSON file to create a Genres table in the database. Finally, I wanted to visualize my queries, so I created a Django web app and integrated it with a React frontend. 


Data I wanted to visualize:
- What was my most streamed title of all time?
- Most streamed movie?
- Most streamed show?
- How many minutes I’ve spent all time streaming titles?
- What were my top 5 most streamed titles?
- What day I watched the most titles? And what title was it?
- Did I watch more titles by tv, phone, or laptop?
- Usual time of day I watched titles (night, morning, afternoon)
- What was my most watched genre?
- What were my top 5 genres?
