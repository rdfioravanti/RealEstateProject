from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate dummy users'

    def handle(self, *args, **kwargs):
        # Dummy data for users
        user_data = [
            {
                'username': 'user1',
                'email': 'user1@example.com',
                'password': 'password1',
                'first_name': 'John',
                'last_name': 'Doe'
            },
            {
                'username': 'user2',
                'email': 'user2@example.com',
                'password': 'password2',
                'first_name': 'Jane',
                'last_name': 'Smith'
            },
            # Add more entries as needed
        ]

        # Create users
        for data in user_data:
            User.objects.create_user(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated users'))
