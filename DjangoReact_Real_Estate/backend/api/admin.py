# app_name/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Property

# Admin for Property model
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'owner', 'price', 'bedrooms', 'bathrooms')
    list_filter = ('owner', 'bedrooms', 'bathrooms')
    search_fields = ('address', 'owner__username')
    raw_id_fields = ('owner',)