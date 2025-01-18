from django.shortcuts import render
from .models import ViewingActivity
from django.db.models import Count, Sum, When, Case, Value, CharField
from django.db.models.functions import Substr

"""Queries that make up Netflix Wrapped"""
def home(request):
    profile_name = "Chiamaka"  
    # Query to get most streamed TITLE of all time
    most_streamed = (ViewingActivity.objects
                     .filter(profile_name=profile_name)
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')
                     .first()
                     )
    # Query that gets the top 5 most streamed titles
    top_five = (ViewingActivity.objects
                     .filter(profile_name=profile_name)
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')[:5]
                     )
    # Query that gets the most streamed movie
    most_streamed_movie = (ViewingActivity.objects
                            .filter(profile_name=profile_name)
                            .exclude(video_type="TV Show")
                            .values("title")
                            .annotate(title_count=Count("title"))
                            .order_by('-title_count')
                            .first()
                            )
    # Query that gets the most streamed TV show
    most_streamed_show = (ViewingActivity.objects
                          .filter(profile_name=profile_name)
                          .exclude(video_type="Movie")
                          .annotate(show_name=Substr("title", 1,10))
                          .values("title")
                          .annotate(title_count=Count("title"))
                          .order_by('-title_count')
                          .first()
                          )
    # Query that gets minutes spent streaming all-time
    all_time_minutes = (ViewingActivity.objects
                        .filter(profile_name=profile_name)
                        .aggregate(total_duration=Sum("duration"))
                        )
    # Query that gets minutes per year
    minutes_per_year = (ViewingActivity.objects
                        .filter(profile_name=profile_name)
                        .exclude(start_time__year="2025")
                        .values("start_time__year")
                        .annotate(minutes_sum=Sum("duration"))
                        )
    # Query that gets the year with most streaming minutes
    most_year = max(minutes_per_year, key=lambda x: x["minutes_sum"])

    # Query to gets day all time with most streaming minutes
    day_all_time = (ViewingActivity.objects
                    .filter(profile_name=profile_name)
                    .values("start_time__date", "title")
                    .annotate(minutes_sum=Sum("duration"))
                    .order_by("-minutes_sum")
                    .first()
                    )
    # Query that tells me which device I watch the most on
    most_streamed_device = (ViewingActivity.objects
                     .filter(profile_name=profile_name)
                     .values("device_type")
                     .annotate(device_count=Count("device_type"))
                     .order_by('-device_count')
                     .first()
                     )  
    #Query that tells me whether I watch more movies or TV shows
    movie_vs_show = (ViewingActivity.objects
                     .filter(profile_name=profile_name)
                     .values("video_type")
                     .annotate(type_count=Count("video_type"))
                     .order_by('-type_count')
                     .first()
                     )
    # Query that tells me usual time of day I most watch Netflix
    time_of_day = (ViewingActivity.objects
                   .filter(profile_name=profile_name)
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
    }

    return render(request, "wrapped.html", context)