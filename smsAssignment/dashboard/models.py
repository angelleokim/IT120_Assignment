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

    