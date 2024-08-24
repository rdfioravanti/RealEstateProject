from django.db import models
from django.conf import settings
from django.utils import timezone

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    built_area = models.PositiveIntegerField(default=0, help_text="Built area in square feet")
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Lot size in acres")
    year_built = models.PositiveIntegerField(default=timezone.now().year, help_text="Year the property was built")
    is_featured = models.BooleanField(default=False, help_text="Is this property featured?")
    garage_spaces = models.PositiveIntegerField(default=0, help_text="Number of garage spaces")
    is_published = models.BooleanField(default=True, help_text="Is this property published and visible?")
    created_at = models.DateTimeField(default=timezone.now, help_text="Date and time when the property was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the property was last updated")

    def __str__(self):
        return self.address
