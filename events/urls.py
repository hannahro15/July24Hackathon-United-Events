from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path('add_event/', add_event, name='add_event'),
    path("like/<int:event_id>/", views.like_event, name="like-event"),
    path("api/", views.event_list, name="event-list"),
]
