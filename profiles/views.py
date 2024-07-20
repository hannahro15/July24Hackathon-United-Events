from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from allauth.account.models import EmailAddress
from .models import Profile
from events.models import Event


@login_required
def profile(request):
    """
    Retrieve the current user's profile.
    Grabs their "interested events" as well.
    Allows updating only username/email address, while keeping "unique" still.
    """
    profile = get_object_or_404(Profile, user=request.user)
    interested_events = profile.interested_events.annotate(total_interested=Count("interested_users"))  # noqa

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exclude(pk=request.user.pk).exists():  # noqa
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exclude(pk=request.user.pk).exists():  # noqa
            messages.error(request, "Email already exists.")
        else:
            request.user.username = username
            request.user.email = email
            request.user.save()

            email_address, created = EmailAddress.objects.get_or_create(
                user=request.user, defaults={"email": email, "verified": True, "primary": True}  # noqa
            )
            if not created:
                email_address.email = email
                email_address.save()

            messages.success(request, "Profile updated successfully.")

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "events": interested_events,
    }
    return render(request, template, context)
