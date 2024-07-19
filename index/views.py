from django.shortcuts import render
# from django.contrib import messages


def index(request):
    """
    Renders the main page.
    """
    # messages.success(request, "Test")
    template = "index/index.html"
    context = {}
    return render(request, template, context)
