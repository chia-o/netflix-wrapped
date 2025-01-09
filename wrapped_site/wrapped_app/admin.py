from django.contrib import admin
from .models import Titles, ViewingActivity

# Register your models here.
class TitlesAdmin(admin.ModelAdmin):
    list_display = [
        "title_id",
        "title",
    ]
class ViewingAdmin(admin.ModelAdmin):
    list_display = [
        "profile_name",
        "start_time",
        "duration",
        "title",
        "video_type",
        "device_type",
        "latest_bookmark",
        "title_id",
        "session_id",
    ]

admin.site.register(Titles, TitlesAdmin)
admin.site.register(ViewingActivity, ViewingAdmin)