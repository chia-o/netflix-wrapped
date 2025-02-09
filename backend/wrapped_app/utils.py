from collections import Counter
from .models import ViewingActivity, Titles

def genre_count(profile_name):
    # fetching genres from Viewing Activity
    session_data = (ViewingActivity.objects
                .filter(profile_name=profile_name)
                .values('session_id', 'title')
                )
    # retrieving title id, title and genre only
    fetched_records = Titles.objects.all().values('title_id', 'title', 'genre')

    title_genre_map = {}

    for row in fetched_records:
        genres = row['genre']

        if genres:
            genres = genres.split(", ")
            title_genre_map[row['title']] = genres
        else:
            title_genre_map[row['title']] = genres
        # example: 'Bojack Horseman': ['Comedy', 'Drama'],

    results = []

    for data in session_data:
        title_before_colon = data['title_before_colon'].split(":")[0]

        print(f"Title before colon: '{title_before_colon}'")


        if title_before_colon in title_genre_map:
            results.extend(title_genre_map[title_before_colon])

        else:
            print(f"Warning: No genres found for title: '{title_before_colon}'")
    
    result_counter = Counter(results)

    most_watched = result_counter.most_common(1) # top watched genre
    top_five = result_counter.most_common(5) # top five

    return most_watched, top_five