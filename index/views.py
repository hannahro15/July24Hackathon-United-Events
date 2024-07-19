from .forms import ( UnitedSignUpForm, UnitedSignInForm, ContactForm
)
from django.contrib.auth.decorators import login_required
from .models import UnitedUserProfile, ContactMessage
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the main page of the site using the 'index/index.html' template.
    It provides an empty context dictionary for potential future use.
    """
    template = "index/index.html"
    context = {}
    return render(request, template, context)


def contact(request):
    """
    Handles incoming contact messages or displays the form.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            contact_message.save()

            messages.success(
                request, "Thank you for contacting us! "
                "We will get back to you soon.")
            return redirect('index')
        else:
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def my_signup_view(request):
    """
    Handle user signup, create a user, log events,
    and redirect to index on success. Render signup
    form with errors if invalid.
    """
    if request.method == 'POST':
        form = UnitedSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            logger.info(f"New user signed up: {user.username}")

            if form.cleaned_data.get('newsletter_subscribe'):
                messages.info(
                    request, 'Thank you for registering to our newsletter.'
                )

            return redirect('index')
        else:
            logger.warning("Signup form validation failed")
            for field, errors in form.errors.items():
                logger.debug(f"{field}: {errors}")
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = UnitedSignUpForm()
    return render(request, 'account/signup.html', {'form': form})
