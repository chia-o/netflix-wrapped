from django.core.management.base import BaseCommand
from backend.wrapped_app.models import Titles, Genres

class Command(BaseCommand):
    help = "Populates the title_genre table with the many-to-many relationship"

    def handle(self, *args, **kwargs):
        titles = Titles.objects.all()

        for title in titles:
            genre_names = title.genre

            if genre_names:
                genre_names_list = genre_names.split(", ")

                genres = Genres.objects.filter(name__in=genre_names_list)

                title.genre.set(genres)
                
                title.save()
        
        self.stdout.write(self.style.SUCESS("Successfully populated titles_genre table!"))
