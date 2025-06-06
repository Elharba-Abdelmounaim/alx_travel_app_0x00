from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING('Database already seeded. Skipping.'))
            return

        locations = ['Marrakech', 'Casablanca', 'Tangier', 'Rabat', 'Agadir']
        titles = ['Cozy Apartment', 'Beach House', 'Mountain Cabin', 'Luxury Villa', 'Modern Studio']

        for _ in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description='This is a sample description for a travel listing.',
                price_per_night=random.uniform(30, 200),
                location=random.choice(locations)
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created listing: {listing.title}'))
