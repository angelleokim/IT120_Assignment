from django.contrib import admin

# Register your models here.
# Import the Message model from the current app's models module.
from .models import Message


# Define a custom admin class for the Message model.
class MessageAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view of the admin panel.
    list_display = ['team_name', 'event_name', 'event_date', 'event_time']  # Fixed field name here