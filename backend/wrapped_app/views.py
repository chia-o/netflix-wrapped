from django.shortcuts import render
from .models import ViewingData
from django.db.models import Count, Sum, When, Case, Value, CharField
from django.db.models.functions import Substr
from django.db import connection

"""Queries that make up Netflix Wrapped"""
def home(request):
    # Query to get most streamed TITLE of all time
    most_streamed = (ViewingData.objects
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')
                     .first()
                     )
    # Query that gets the top 5 most streamed titles
    top_five = (ViewingData.objects
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')[:5]
                     )
    # Query that gets the most streamed movie
    most_streamed_movie = (ViewingData.objects
                            .exclude(video_type="TV Show")
                            .values("title")
                            .annotate(title_count=Count("title"))
                            .order_by('-title_count')
                            .first()
                            )
    # Query that gets the most streamed TV show
    most_streamed_show = (ViewingData.objects
                          .exclude(video_type="Movie")
                          .annotate(show_name=Substr("title", 1,10))
                          .values("title")
                          .annotate(title_count=Count("title"))
                          .order_by('-title_count')
                          .first()
                          )
    # Query that gets minutes spent streaming all-time
    all_time_minutes = (ViewingData.objects
                        .aggregate(total_duration=Sum("duration"))
                        )
    # Query that gets minutes per year
    minutes_per_year = (ViewingData.objects
                        .exclude(start_time__year="2025")
                        .values("start_time__year")
                        .annotate(minutes_sum=Sum("duration"))
                        )
    # Query that gets the year with most streaming minutes
    most_year = max(minutes_per_year, key=lambda x: x["minutes_sum"])

    # Query to gets day all time with most streaming minutes
    day_all_time = (ViewingData.objects
                    .values("start_time__date", "title")
                    .annotate(minutes_sum=Sum("duration"))
                    .order_by("-minutes_sum")
                    .first()
                    )
    # Query that tells me which device I watch the most on
    most_streamed_device = (ViewingData.objects
                     .values("device_type")
                     .annotate(device_count=Count("device_type"))
                     .order_by('-device_count')
                     .first()
                     )  
    #Query that tells me whether I watch more movies or TV shows
    movie_vs_show = (ViewingData.objects
                     .values("video_type")
                     .annotate(type_count=Count("video_type"))
                     .order_by('-type_count')
                     .first()
                     )
    # Query that tells me usual time of day I most watch Netflix
    time_of_day = (ViewingData.objects
                   .annotate(
                       time_of_day=Case(
                                    When(start_time__hour__lt=12, then=Value("Morning")), 
                                    When(start_time__hour__gte=12, start_time__hour__lt=17, then=Value("Afternoon")),
                                    When(start_time__hour__gte=17, start_time__hour__lt=20, then=Value("Evening")),
                                    default=Value("Night"),
                                    output_field=CharField()
                                    )
                            )
                   .values("time_of_day")
                   .annotate(hour_count=Count("time_of_day"))
                   .order_by('-hour_count')
                   )
    # Query that gives me the time of day category with the most views
    most_time_of_day = max(time_of_day, key=lambda x: x["hour_count"])

    # Query that gets the most watched genre
    top_genre = """
        SELECT 
            TRIM(genre) AS genre,
        FROM (
            SELECT 
                vd.session_id,
                regexp_split_to_table(td.genre, ',') AS genre
            FROM viewing_data vd
            JOIN title_data td ON vd.title_id = td.title_id
            WHERE td.genre IS NOT NULL
        ) AS genre_data
        GROUP BY TRIM(genre)
        ORDER BY view_count DESC
        LIMIT 1;
    """

    # Query that gets the most watched genre
    top_five_genres = """
        SELECT 
            TRIM(genre) AS genre,
        FROM (
            SELECT 
                vd.session_id,
                regexp_split_to_table(td.genre, ',') AS genre
            FROM viewing_data vd
            JOIN title_data td ON vd.title_id = td.title_id
            WHERE td.genre IS NOT NULL
        ) AS genre_data
        GROUP BY TRIM(genre)
        ORDER BY view_count DESC
        LIMIT 5;
    """

    with connection.cursor() as cursor:
        cursor.execute(top_genre)
        top_genre = cursor.fetchone()

        cursor.execute(top_five_genres)
        five_genres = cursor.fetchall()

    

    context = {
        "most_streamed": most_streamed,
        "top_five": top_five,
        "most_streamed_movie": most_streamed_movie,
        "most_streamed_show": most_streamed_show,
        "all_time_minutes": all_time_minutes,
        "minutes_per_year": minutes_per_year,
        "most_year": most_year,
        "day_all_time": day_all_time,
        "most_streamed_device": most_streamed_device,
        "movie_vs_show": movie_vs_show,
        "time_of_day": time_of_day,
        "most_time_of_day": most_time_of_day,
        "top_genre": top_genre,
        "top_five_genres": top_five_genres

    }

    return render(request, "wrapped.html", context)