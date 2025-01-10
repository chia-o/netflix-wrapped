""" This script is to remove trailers and categorize tv shows and movies, which I didn't do before connecting to the database. """
"""BaseCommand is the base class for making my own management commands. """
from django.core.management.base import BaseCommand
from wrapped_app.models import ViewingActivity

class Command(BaseCommand):
    help = "Classifies whether each title is a movie or tv show"

    def handle(self, *args, **kwargs):
        # Remove trailers
        deleted, _ = ViewingActivity.objects.filter(title__icontains="hook").delete() # need to add the _ so the dictionary isn't printed to terminal
        self.stdout.write(self.style.SUCCESS("{deleted} trailers have been removed."))

        #Classify titles into tv shows and movies
        for title in ViewingActivity.objects.all():
            if "Season" in title.title or "Episode" in title.title:
                title.video_type = "TV Show"
            else:
                title.video_type = "Movie"
            title.save()
        self.stdout.write(self.style.SUCCESS("Titles have been classified!"))

        # Classify device types
        for device_type in ViewingActivity.objects.all():
            if "Q60A" in device_type.device_type or "TV" in device_type.device_type or "LG" in device_type.device_type:
                device_type.device_type = "TV"
            elif "iPhone" in device_type.device_type:
                device_type.device_type = "Phone"
            elif "iPad" in device_type.device_type or "iPod" in device_type.device_type:
                device_type.device_type = "Tablet"
            elif "PC" in device_type.device_type or "MAC" in device_type.device_type or "Mac" in device_type.device_type:
                device_type.device_type = "Computer"
            else:
                device_type.device_type = "Blu-ray Player"
            device_type.save()
        self.stdout.write(self.style.SUCCESS("Device types have been classified!"))