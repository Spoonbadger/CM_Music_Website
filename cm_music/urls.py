from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.login, name="logout"),
    path("register", views.register, name="register"),
    path("bio", views.bio, name="bio"),
    path("contact", views.contact, name="contact"),
    path("links", views.links, name="links"),
    path("music", views.music, name="music"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)