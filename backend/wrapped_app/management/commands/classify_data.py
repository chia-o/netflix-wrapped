""" This script is to remove trailers and categorize tv shows and movies, which I didn't do before connecting to the database. """
"""BaseCommand is the base class for making my own management commands. """
from django.core.management.base import BaseCommand
from backend.wrapped_app.models import ViewingActivity, Titles, ViewingData, TitleData
from django.db.models import Q
import re

class Command(BaseCommand):
    help = "Classifies whether each title is a movie or tv show"

    def handle(self, *args, **kwargs):
        # Remove trailers, clips, teasers, recaps
        deleted, _ = ViewingActivity.objects.filter(Q(title__icontains="hook") | Q(title__icontains="Clip") | Q(title__icontains="Teaser") | Q(title__icontains="CLM") | Q(title__icontains="Recap")).delete() # need to add the _ so the dictionary isn't printed to terminal
        self.stdout.write(self.style.SUCCESS("{deleted} trailers have been removed."))

        """
        # Refactor title_id to define a distinct movie or repeating tv show 
        for title in ViewingActivity.objects.all():
            # will return the part before : for shows, or full name for movies
            name = title.title.split(":")[0] if ":" in title.title else title.title

            # will get or create a Titles object for each title
            title_obj,created = Titles.objects.get_or_create(title=name, defaults={'video_type': title.video_type})

            # to assign the new title_id and save it
            title.title_id = title_obj
            title.save()
        
        self.stdout.write(self.style.SUCCESS("Title IDs have been assigned!"))
        """

        #Classify titles into tv shows and movies
        for title in TitleData.objects.all():
            if re.search(r': (Season \d+|Limited Series)', title.title, re.IGNORECASE):
                title.category = "TV Show"
            else:
                title.category = "Movie"
            title.save()
        self.stdout.write(self.style.SUCCESS("Titles have been classified!"))
        
        """Do NOT RUN!!!!!!!!!
        # Classify device types
        for device_type in ViewingData.objects.all():
            if "Q60A" in device_type.device_type or "TV" in device_type.device_type or "LG" in device_type.device_type:
                device_type.device_type = "TV"
            elif "iPhone" in device_type.device_type:
                device_type.device_type = "Phone"
            elif "iPad" in device_type.device_type or "iPod" in device_type.device_type:
                device_type.device_type = "Tablet"
            elif "PC" in device_type.device_type or "MAC" in device_type.device_type or "Mac" in device_type.device_type:
                device_type.device_type = "Computer"
            elif "Blur-ray Player" in device_type.device_type:
                device_type.device_type = "Blu-ray Player"
            else:
                device_type.device_type = None
            
            device_type.save()
        
        self.stdout.write(self.style.SUCCESS("Device types have been classified!"))
        """

        
        # Update ViewingData with title_id from Titles
        """
        for data in ViewingData.objects.all():
            name = data.title.split(":")[0] if ":" in data.title else data.title
            try:
                title_obj = TitleData.objects.get(title=name)
                data.title_id = title_obj
                data.save()
            except TitleData.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Title '{name}' not found in Titles table."))

        self.stdout.write(self.style.SUCCESS("ViewingData has been updated with title IDs!"))
        """
        