from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin configuration for Event
    """
    list_display = ('name', 'start_date', 'location')
