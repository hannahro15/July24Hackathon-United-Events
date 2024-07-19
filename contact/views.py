from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Handles incoming contact messages or displays the form.
    """
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for contacting United Events! "
                "We will get back to you soon."
            )
            return redirect('index')
        else:
            messages.error(request, "Error: Please Try Again.")

    template = "contact/contact.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
