from django import forms
from django.forms.widgets import (
    EmailInput, NumberInput, PasswordInput, TextInput, URLInput
)
from .models import Contact

# placeholders for Bootstrap floating-label functionality
# valid type: email, number, password, search, tel, text, url
valid_types = (EmailInput, NumberInput, PasswordInput, TextInput, URLInput)


class ContactForm(forms.ModelForm):
    """
    A form for users to submit contact information and a message.
    """
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

    class Meta:
        model = Contact
        fields = (
            "name", "email", "message"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            this_widget = self.fields[field].widget
            if isinstance(this_widget, valid_types):
                this_widget.attrs["placeholder"] = field
            this_widget.attrs["class"] = "form-control"
