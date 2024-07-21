from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import handler400, handler403, handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("index.urls")),
    path("contact/", include("contact.urls")),
    path("events/", include("events.urls")),
    path("profile/", include("profiles.urls")),
]

handler400 = "united.views.handler400"
handler403 = "united.views.handler403"
handler404 = "united.views.handler404"
handler500 = "united.views.handler500"
