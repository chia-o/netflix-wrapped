from django.core.management.base import BaseCommand
from backend.wrapped_app.models import ViewingData, TitleData
import re

def clean_title(title):
    if "Episode" in title:
        cleaned_title = re.sub(r': (Part|Series|Episode|Volume|Collection|Chapter|Vol|Limited Series) \d+.*', '', title, flags=re.IGNORECASE)
        
        parts = cleaned_title.split(":")
        if len(parts) > 1:
            cleaned_title = ":".join(parts[:2]).strip()
        else:
            cleaned_title = parts[0].strip()
    else:
        cleaned_title = title
    return cleaned_title

class Command(BaseCommand):
    help = "This is to extract tv shows and movies from ViewingData into TitleData table"

    def handle(self, *args, **kwargs):
        viewing_data = ViewingData.objects.all()

        for data in viewing_data:
            cleaned_title = clean_title(data.title)
            TitleData.objects.create(
                title=cleaned_title
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated TitleData table!"))