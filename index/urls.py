from django.urls import path, include
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'accounts/',
        include('allauth.urls')
    ),
    path(
        'signup/',
        views.my_signup_view,
        name='my_signup_view'
    ),
    path(
        'contact/',
        views.contact,
        name='contact'
    ),
]
