from django.urls import path

from . import views

## make sure you type urlpatterns 
urlpatterns = [
    path("", views.index , name="index")
]