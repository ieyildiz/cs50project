from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("eren", views.eren, name = "eren"),
    path("<str:name>", views.greet, name="greet")
]