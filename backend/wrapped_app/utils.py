from collections import Counter
from backend.wrapped_app.models import ViewingActivity, Titles, Genres



def genre_count(profile_name):

    title_genre_map = {}

    # Gets all titles with their genres
    titles = Titles.objects.all()

    for title in titles:
        genres = title.genre.all()
        genre_list = [genre.name for genre in genres]
        title_genre_map[title.title] = genre_list

    results = []
    session_data = (ViewingActivity.objects
            .filter(profile_name='Chiamaka')
            .values('session_id', 'title')
            )
    # 
    for data in session_data:
        # gets the full string and then splits at the semi-colon, returning only the first part
        title_name = data['title'].split(":")[0] # get the tv show name

        print(f"Title before colon: '{title_name}'")

        # add the genre(s) for each title to results 
        if title_name in title_genre_map:
            genres = title_genre_map[title_name]
            results.extend(genres) 

    
    result_counter = Counter(results)
    most_watched = result_counter.most_common(1) # top watched genre
    top_five = result_counter.most_common(5) # top five

    return most_watched, top_five

    
if __name__ == "__main__":
    titles_genre()
    profile_name = 'Chiamaka'
    most_watched, top_five = genre_count(profile_name)
    print(f"Most Watched Genre: {most_watched}")
    print(f"Top 5 Genres: {top_five}")
