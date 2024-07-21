from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path('add_event/', views.add_event, name='add-event'),
    path('manage/', views.manage_events, name='manage-events'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete-event'),  # noqa
    path('edit_event/<int:event_id>/', views.edit_event, name='edit-event'),
    path("like/<int:event_id>/", views.like_event, name="like-event"),
    path("api/", views.event_list, name="event-list"),
]
