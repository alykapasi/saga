from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile, name="profile"),
    path("main/", views.applet, name="applet"),
    path("todo/", views.todo, name="todo"),
]