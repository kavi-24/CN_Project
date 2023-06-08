from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("credits", views.credits),
    path("app", views.app),
]