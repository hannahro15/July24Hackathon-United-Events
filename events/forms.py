from django import forms
from .models import Event


class DateInput(forms.DateInput):
    input_type = "date"


class EventForm(forms.ModelForm):
    """
    The form to allow admin users to add events.
    """
    class Meta:
        model = Event
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }
        fields = (
            'name', 'start_date', 'end_date', 'location',
            'description', 'highlights', 'accessibility',
            'ticket_info', 'additional_notes', 'website'
        )
        labels = {
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'accessibility': 'Accessibility (Optional)',
            'ticket_info': 'Ticket Information',
            'additional_notes': 'Additional Notes (Optional)',
            'website': 'Website'
        }