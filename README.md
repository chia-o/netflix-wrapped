# netflix-wrapped
A project that creates a Spotify Wrapped dupe for my Netflix viewing history from 2012 - 2025. 

I wrote the app in Python and created my database from a CSV file in Postgresql. I wanted to visualize my queries, so I created a Django web app and also gained practice with ORMs and the QuerySet API. I designed a template in Webflow and will export the HTML to Django.

The viewing history CSV file didn't come classified by genre, so I plan to either use the tMDB API or create a web scraper to add genres, and build a title recommender ML model. In the future, I might also generalize the project more, and query databases of my data from other streaming platforms, if possible.

Questions I wanted to ask:
- What was my most streamed title of all time?
- Most streamed movie?
- Most streamed show?
- How many minutes I’ve spent all time streaming titles?
- What were my top 5 most streamed titles?
- What day I watched the most titles? And what title was it?
- Did I watch more titles by tv, phone, or laptop?
- Usual time of day I watched titles (night, morning, afternoon)
