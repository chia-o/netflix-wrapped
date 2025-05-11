from .models import ViewingData
from django.db.models import Count, Sum, When, Case, Value, CharField
from django.db.models.functions import Substr
from django.db import connection
from django.http import JsonResponse

"""Queries that make up Netflix Wrapped"""


# Query to get most streamed TITLE of all time
def most_streamed(request):
    data = (ViewingData.objects
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')
                     .first()
                     )
    return JsonResponse(data)

# Query that gets the top 5 most streamed titles
def top_five(request):
    data = (ViewingData.objects
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')[:5]
                     )
    return JsonResponse(data)

# Query that gets the most streamed movie
def most_streamed_movie(request):
    data = (ViewingData.objects
                            .exclude(video_type="TV Show")
                            .values("title")
                            .annotate(title_count=Count("title"))
                            .order_by('-title_count')
                            .first()
                            )
    return JsonResponse(data) 

# Query that gets the most streamed TV show
def most_streamed_show(request):
    data = (ViewingData.objects
                          .exclude(video_type="Movie")
                          .annotate(show_name=Substr("title", 1,10))
                          .values("title")
                          .annotate(title_count=Count("title"))
                          .order_by('-title_count')
                          .first()
                          )
    return JsonResponse(data) 

# Query that gets minutes spent streaming all-time
def all_time_minutes(request):
    data = (ViewingData.objects
                        .aggregate(total_duration=Sum("duration"))
                        )
    return JsonResponse(data)   

# Query that gets minutes per year
def minutes_per_year(request):
    data = (ViewingData.objects
                        .exclude(start_time__year="2025")
                        .values("start_time__year")
                        .annotate(minutes_sum=Sum("duration"))
                        )
    return JsonResponse(data)  

# Query that gets the year with most streaming minutes
def most_year(request):
    data = max(minutes_per_year, key=lambda x: x["minutes_sum"])
    return JsonResponse(data)

# Query to gets day all time with most streaming minutes
def day_all_time(request):
    data = (ViewingData.objects
                    .values("start_time__date", "title")
                    .annotate(minutes_sum=Sum("duration"))
                    .order_by("-minutes_sum")
                    .first()
                    )
    return JsonResponse(data)   

# Query that tells me which device I watch the most on
def most_streamed_device(request):
    most_streamed_device = (ViewingData.objects
                     .values("device_type")
                     .annotate(device_count=Count("device_type"))
                     .order_by('-device_count')
                     .first()
                     )
    return JsonResponse(data)    

def movie_vs_show(request):
    data = (ViewingData.objects
                     .values("video_type")
                     .annotate(type_count=Count("video_type"))
                     .order_by('-type_count')
                     .first()
                     )
    return JsonResponse(data)   

def time_of_day(request):
    data = (ViewingData.objects
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
    return JsonResponse(data)

# Query that gives me the time of day category with the most views
def most_time_of_day(request):
    data = max(time_of_day, key=lambda x: x["hour_count"])
    return JsonResponse(data) 

# Query that gives my top genre
def top_genre(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                TRIM(genre) AS genre
            FROM (
                SELECT 
                    vd.session_id,
                    regexp_split_to_table(td.genre, ',') AS genre
                FROM viewing_data vd
                JOIN title_data td ON vd.title_id = td.title_id
                WHERE td.genre IS NOT NULL
            ) AS genre_data
            GROUP BY TRIM(genre)
            ORDER BY COUNT(*) DESC
            LIMIT 1;
        """)
        row = cursor.fetchone()
        data = {"genre": row[0]} if row else {"error": "No genre data found"}
    return JsonResponse(data, safe=False)

# Query that gets the most watched genre
def top_five_genres(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                TRIM(genre) AS genre
            FROM (
                SELECT 
                    vd.session_id,
                    regexp_split_to_table(td.genre, ',') AS genre
                FROM viewing_data vd
                JOIN title_data td ON vd.title_id = td.title_id
                WHERE td.genre IS NOT NULL
            ) AS genre_data
            GROUP BY TRIM(genre)
            ORDER BY COUNT(*) DESC
            LIMIT 5;
        """)
        rows = cursor.fetchall()
        if rows:
            data = [row[0] for row in rows]
        else:
            data = {"error": "No genre data found"}
    return JsonResponse(data, safe=False)

def home(request):
    return JsonResponse({
        "message": "Welcome to the Netflix Stats API!",
        "endpoints": [
            "/data/top-genre/",
            "/data/top-five-genre/",
            "/data/most-streamed/",
            # Add other API endpoints here
        ]
    })