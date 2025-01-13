# netflix-wrapped
Something I've wanted to make for years...
 a Spotify Wrapped dupe for my Netflix viewing history from 2012 - 2025. 

I wrote the app in Python and created my database from a CSV file in Postgresql. I wanted to visualize my queries, so I created a Django web app and also gained practice with ORMs and the QuerySet API.

The viewing history CSV file didn't come classified by genre, so I plan to either use the tMDB API or create a web scraper to add genres, and build a title recommender ML model. In the future, I might also generalize the project more, and query databases of my data from other streaming platforms, if possible.
