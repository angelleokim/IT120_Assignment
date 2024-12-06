from django.db import models
import os 
from twilio.rest import Client
from django.utils import timezone

# Define a callable function for the default  time value
def get_current_time():
    return timezone.now().time()


class Message(models.Model):
     # Define a 'team_name' field to store the name of the team, with a default value.
    team_name = models.CharField(max_length=100, default='Default Team')  # Provide a default value for team_name

    # Define an 'event_name' field to store the name of the event.
    event_name = models.CharField(max_length=100, default='Default Team')

     # Define an 'event_date' field to store the date of the event. Default to today's date.
    event_date = models.DateField(default=timezone.now)  # Default to the current date

    # Define an 'event_time' field to store the time of the event. Use the callable function for the default value.
    event_time = models.TimeField(default=get_current_time)  # Default to the current time using a callable function

    # String representation of the model; returns the team name and event name.
    def __str__(self):
        return f"{self.team_name} - {self.event_name}"

    # Overriding the save method to include custom behavior when saving an object.
    def save(self, *args, **kwargs):


        # Call the parent class's save method to ensure normal behavior.
        return super().save(*args, **kwargs)
