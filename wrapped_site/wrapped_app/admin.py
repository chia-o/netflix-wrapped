from django.contrib import admin
from .models import ViewingActivity

# Register your models here.
"""
class TitlesAdmin(admin.ModelAdmin):
    list_display = [
        "title_id",
        "title",
    ]
"""
class ViewingAdmin(admin.ModelAdmin):
    list_display = [
        "profile_name",
        "start_time",
        "duration",
        "title",
        "video_type",
        "device_type",
        "latest_bookmark",
        "session_id",
    ]

#admin.site.register(Titles, TitlesAdmin)
admin.site.register(ViewingActivity, ViewingAdmin)