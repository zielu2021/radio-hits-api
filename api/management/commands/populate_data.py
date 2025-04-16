import random
from django.core.management.base import BaseCommand
from api.models import Artist, Hit

class Command(BaseCommand):
    help = 'Populates the database with initial data (artists and hits)'
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data population...')
       
        # Existing data deletion
        Hit.objects.all().delete()
        Artist.objects.all().delete()
       
        # Artists
        artists = [
            Artist.objects.create(first_name='John', last_name='Doe'),
            Artist.objects.create(first_name='Jane', last_name='Smith'),
            Artist.objects.create(first_name='Michael', last_name='Johnson'),
        ]
       
        self.stdout.write(self.style.SUCCESS(f'Created {len(artists)} artists'))
       
        # Titles
        hit_titles = [
            'Summer Breeze', 'Midnight Moon', 'Electric Dreams', 'Ocean Waves',
            'City Lights', 'Mountain High', 'Desert Rose', 'River Flow',
            'Starry Night', 'Sunset Boulevard', 'Morning Coffee', 'Evening Rain',
            'Autumn Leaves', 'Winter Snow', 'Spring Flowers', 'Golden Sun',
            'Silver Moon', 'Diamond Sky', 'Ruby Heart', 'Emerald Forest',
            'Sapphire Sea', 'Amber Glow', 'Crystal Clear', 'Velvet Night'
        ]
       
        # Hit creation
        hits = []
        for i, title in enumerate(hit_titles[:20]):
            artist = random.choice(artists)
            hit = Hit.objects.create(
                title=title,
                artist=artist
            )
            hits.append(hit)
       
        self.stdout.write(self.style.SUCCESS(f'Created {len(hits)} hits'))
        self.stdout.write(self.style.SUCCESS('Data population completed successfully!'))