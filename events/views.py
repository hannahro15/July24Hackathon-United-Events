from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Event
from profiles.models import Profile
from .forms import EventForm


def events(request):
    """
    Displays the events calendar.
    - FullCalendar uses the first/last events (if any)
    - Builds calendar using start/end date, and full-month display
    """
    current_date = datetime.now()
    first_event = Event.objects.filter(start_date__gte=current_date).order_by("start_date").first()
    last_event = Event.objects.filter(start_date__gte=current_date).order_by("start_date").last()

    # Get the first day of the month of the first (next) event
    start_date = first_event.start_date if first_event else current_date
    end_date = last_event.end_date if last_event else current_date
    first_of_current_month = current_date.replace(day=1)

    # Get the last day of the month of the last event
    last_of_last_event_month = end_date.replace(day=1)
    last_of_last_event_month = (last_of_last_event_month + timedelta(days=32)).replace(day=1) - timedelta(days=0)

    template = "events/events.html"
    context = {
        "first_event": first_event,
        "last_event": last_event,
        "start_date": first_of_current_month.strftime("%Y-%m-%d"),
        "end_date": last_of_last_event_month.strftime("%Y-%m-%d"),
        "events_exist": Event.objects.exists()
    }

    return render(request, template, context)


@login_required
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    profile = request.user.profile
    if event in profile.interested_events.all():
        messages.info(request, "🌈 One less event in your rainbow. Keep shining, fabulous! ✨")  # noqa
        profile.interested_events.remove(event)
    else:
        messages.success(request, "🌈 Event added to your list! Get ready to spread the love and sparkle! ✨")  # noqa
        profile.interested_events.add(event)

    # Redirect to the previous page
    return redirect(request.META.get("HTTP_REFERER", "events"))


@login_required
def add_event(request):
    """
    Allow admin users to add events to the site.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access Denied: Invalid Credentials")
        return redirect("index")

    event_form = EventForm(request.POST or None)
    if request.method == "POST":
        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Your event was added successfully')
            return redirect('events')
        else:
            messages.error(
                request,
                'Error: Please try again'
            )

    template = 'events/add_event.html'
    context = {
        'event_form': event_form,
    }
    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """
    Allow admin users to edit events on the site.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access Denied: Invalid Credentials")
        return redirect("index")

    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your event was updated successfully')
            return redirect('manage-events')
        else:
            messages.error(request, 'Error: Please try again')
    else:
        form = EventForm(instance=event)

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event
    }
    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """
    Allow admin users to edit events on the site.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access Denied: Invalid Credentials")
        return redirect("index")

    event = get_object_or_404(Event, id=event_id)

    event.delete()
    messages.success(request, 'Event deleted successfully')
    return redirect('manage-events')


@login_required
def manage_events(request):
    """
    Allow admin manage events.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access Denied: Invalid Credentials")
        return redirect("index")

    events = Event.objects.all()
    today = date.today()

    template = "events/manage_events.html"
    context = {
        "events": events,
        "today": today,
    }

    return render(request, template, context)


def event_list(request):
    """
    API to asynchronously gather event data for FullCalendar.
    """
    current_date = datetime.now().date()
    events = Event.objects.filter(start_date__gte=current_date)
    user = request.user if request.user.is_authenticated else None
    event_list = []
    for event in events:
        is_interested = False
        if user:
            is_interested = event in user.profile.interested_events.all()
        event_list.append({
            "allDay": True,
            "id": event.id,
            "title": event.name,
            "start": event.start_date.isoformat(),
            "end": (event.end_date + timedelta(days=1)).isoformat(),
            "location": event.location,
            "description": event.description,
            "highlights": event.highlights,
            "accessibility": event.accessibility,
            "ticket_info": event.ticket_info,
            "additional_notes": event.additional_notes,
            "website": event.website,
            "is_interested": is_interested,
            "interested_count": event.interested_users.count()
        })
    return JsonResponse(event_list, safe=False)
