from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path("", views.events, name="events"),
    path("like/<int:event_id>/", views.like_event, name="like-event"),
    path("api/", views.event_list, name="event-list"),
=======
    path('', views.events, name='events'),
    path('add_event/', add_event, name='add_event'),
>>>>>>> Stashed changes
]
