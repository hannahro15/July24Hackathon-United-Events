from django.shortcuts import render
from django.contrib import messages


def events(request):
    """
    Displays the events calendar.
    """
    template = "events/events.html"
    context = {}

    return render(request, template, context)
