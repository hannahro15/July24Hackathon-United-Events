from django import forms
from datetime import date
from .models import Event


class DateInput(forms.DateInput):
    """
    Allows the user to choose a date from a calender
    in the Add Event Form.
    """
    input_type = "date"


class EventForm(forms.ModelForm):
    """
    The form to allow admin users to add events.
    """
    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'location',
                  'description', 'highlights', 'accessibility',
                  'ticket_info', 'additional_notes', 'website')
        widgets = {"start_date": DateInput(),
                   "end_date": DateInput()}
        labels = {
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'ticket_info': 'Ticket Information',
            'additional_notes': 'Additional Notes'
        }

