from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
]
