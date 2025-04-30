# Matches title_id by title from title_data to viewing_data
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Update title_id in viewing_data from title_data for both TV Shows and Movies.'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            
            # Update title_id for TV Shows
            self.stdout.write("Updating TV Shows...")
            
            cursor.execute("""
                UPDATE viewing_data vd
                SET title_id = td.title_id
                FROM title_data td
                WHERE 
                  regexp_replace(vd.title, ': (Season|Episode|Limited Series|Series).*$', '', 'g') = td.title
                  AND td.category = 'TV Show';
            """)
            self.stdout.write(self.style.SUCCESS("TV Shows updated."))


            # Update title_id for Movies
            self.stdout.write("Updating Movies...")

            cursor.execute("""
                UPDATE viewing_data vd
                SET title_id = td.title_id
                FROM title_data td
                WHERE 
                  vd.title = td.title
                  AND td.category = 'Movie';
            """)
            self.stdout.write(self.style.SUCCESS("Movies updated."))
