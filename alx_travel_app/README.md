# alx_travel_app# ALX Travel App 0x00

A Django-based travel application for managing listings, bookings, and reviews.

## Setup
1. Clone the repository: `git clone https://github.com/yourusername/alx_travel_app_0x00.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install django djangorestframework`
5. Apply migrations: `python manage.py makemigrations && python manage.py migrate`

## Models
- **Listing**: Represents a travel property (e.g., title, description, location, price_per_night, capacity, owner).
- **Booking**: Tracks user bookings (e.g., listing, user, check-in, check-out, total_price).
- **Review**: Stores user reviews (e.g., listing, user, rating, comment).

## Serializers
- Defined in `listings/serializers.py` for API representation of `Listing` and `Booking` models.

## Seeding the Database
- Run `python manage.py seed` to populate the database with sample listings.
- Check data via `python manage.py shell` and query `Listing.objects.all()`.

## Files
- `listings/models.py`: Database models
- `listings/serializers.py`: API serializers
- `listings/management/commands/seed.py`: Database seeder

## Seeding the Database
- Run `python manage.py seed` to populate the database with sample listings.
- Verify the data using the Django shell:
  ```bash
  python manage.py shell
  from listings.models import Listing
  Listing.objects.all()