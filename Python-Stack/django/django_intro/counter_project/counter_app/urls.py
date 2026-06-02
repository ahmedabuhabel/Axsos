from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("incrementByTwo", views.incrementByTwo),
    path("byAmount", views.byAmount),
    path("reset", views.reset),
    path("destroy_session", views.destroy_session),
]
