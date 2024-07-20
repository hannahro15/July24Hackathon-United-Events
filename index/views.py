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


def team(request):
    """
    Renders the team page.
    """
    # messages.success(request, "Test")
    template = "index/team.html"
    context = {}
    return render(request, template, context)
