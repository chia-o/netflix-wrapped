from django.contrib import admin
from .models import ViewingActivity, Titles, Genres

# Register your models here.
class TitlesAdmin(admin.ModelAdmin):
    list_display = [
        "title_id",
        "title",
        "video_type",
    ]

class ViewingAdmin(admin.ModelAdmin):
    list_display = [
        "title_id",
        "profile_name",
        "start_time",
        "duration",
        "title",
        "video_type",
        "device_type",
        "latest_bookmark",
        "session_id",
    ]

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        "genre",
        "genre_id",
    ]

admin.site.register(Titles, TitlesAdmin)
admin.site.register(ViewingActivity, ViewingAdmin)
admin.site.register(Genres, GenreAdmin)