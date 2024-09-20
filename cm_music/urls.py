from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login", views.login, name="login"),
    # path("logout", views.login, name="logout"),
    # path("register", views.register, name="register"),
    path("bio", views.bio, name="bio"),
    path("contact", views.contact_page, name="contact"),
    path("links", views.links, name="links"),
    path("music", views.music, name="music"),
    path("invest", views.invest, name="invest")
]