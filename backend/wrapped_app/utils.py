from collections import Counter
import os
import sys
import django
import re

sys.path.append('/Users/chiamakaofonagoro/projects/netflix_wrapped')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.wrapped_site.settings')

django.setup()

from backend.wrapped_app.models import ViewingData, Titles

def clean_title(title):
    parts = re.split(r': Season \d+', title)
    return parts[0].strip() if parts else title.strip()

def genre_count():
    # create dictionary for title, genre(s) from Titles table
    title_genre_map = {}
    titles = Titles.objects.all()
    for item in titles:
        genre_list = [genre.genre for genre in item.genre.all()]
        title_genre_map[item.title] = genre_list

    # retrieve title from Viewing_Data, make sure its in dictionary, and then store associated genres found in dict in a list 'results'
    results = []
    viewing_data = ViewingData.objects.values('title') # specialized dictionary
    for data in viewing_data:
        title_name = clean_title(data['title'])
        if title_name in title_genre_map:
            genre_list_data = title_genre_map[title_name] 
            results.extend(genre_list_data)
        else:
            print(f"Title '{title_name}' not found in Title-Genre Map")

    
    result_counter = Counter(results)
    most_watched = result_counter.most_common(1) # top watched genre
    top_five = result_counter.most_common(5) # top five

    return most_watched, top_five

    
if __name__ == "__main__":
    most_watched, top_five = genre_count()
    print(f"Most Watched Genre: {most_watched}")
    print(f"Top 5 Genres: {top_five}")
