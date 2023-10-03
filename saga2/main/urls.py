from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile, name="profile"),
    path("main/", views.applet, name="applet"),
    # path("<int:id>/", views.xtra, name="app"),
    path("todo/", views.todo, name="todo"),
    path("saves/", views.saves, name="saves"),
    path("new/", views.new, name="new"),
    path("xtra/", views.xtra, name="xtra"),
]