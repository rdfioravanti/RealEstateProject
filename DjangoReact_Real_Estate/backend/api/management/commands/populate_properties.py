from django.core.management.base import BaseCommand
from api.models import Property
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate Property model with arbitrary data'

    def handle(self, *args, **kwargs):
        # Dummy data for properties
        property_data = [
            {
                'owner': User.objects.first(),
                'address': '123 Main St',
                'price': 200000.00,
                'bedrooms': 3,
                'bathrooms': 2
            },
            {
                'owner': User.objects.last(),
                'address': '456 Elm St',
                'price': 350000.00,
                'bedrooms': 4,
                'bathrooms': 3
            },
            # Add more entries as needed
        ]

        # Bulk create properties
        properties = []
        for data in property_data:
            property = Property(**data)
            properties.append(property)

        Property.objects.bulk_create(properties)

        self.stdout.write(self.style.SUCCESS('Successfully populated Property model with data'))
