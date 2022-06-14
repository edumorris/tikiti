from cProfile import label
from dataclasses import Field
from pyexpat import model
from django import forms
from .models import Events

class DateInputDisplay(forms.DateInput):
    input_type = "date"

class EventsForm(forms.Form):
    # Form for Events entry
    event_title = forms.CharField(label="Event Title: ", max_length=50)
    event_description = forms.CharField(label="Event Description: ", max_length=200)
    event_date = forms.DateTimeField(label="Event Date: ", widget=DateInputDisplay)
    event_poster = forms.ImageField(label="Event Poster: ")
    active_status = forms.BooleanField(label="Active: ")
    