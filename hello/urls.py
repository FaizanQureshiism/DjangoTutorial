from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path ("faizan", views.faizan, name="faizan")
]