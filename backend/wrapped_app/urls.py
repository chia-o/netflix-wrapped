from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/most-streamed/', views.most_streamed, name='most_streamed'),
    path('data/top-five/', views.top_five, name='top_five'),
    path('data/most-streamed-movie/', views.most_streamed_movie, name='most_streamed_movie'),
    path('data/most-streamed-show/', views.most_streamed_show, name='most_streamed_show'),
    path('data/all-time-minutes/', views.all_time_minutes, name='all_time_minutes'),
    path('data/minutes-per-year/', views.minutes_per_year, name='minutes_pear_year'),
    path('data/most-year/', views.most_year, name='most_year'),
    path('data/day-all-time/', views.day_all_time, name='day_all_time'),
    path('data/most-streamed_device/', views.most_streamed_device, name='most_streamed_device'),
    path('data/movie-vs-show/', views.movie_vs_show, name='movie_vs_show'),
    path('data/time-of-day/', views.time_of_day, name='time_of_day'),
    path('data/most-time-of-day/', views.most_time_of_day, name='most_time_of_day'),
    path('data/top-genre/', views.top_genre, name='top_genre'),
    path('data/top-five-genres/', views.top_five_genres, name='top_five_genres'),
]
