from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("courses/create", views.create_course, name="create_course"),
    path("courses/destroy/<int:course_id>", views.confirm_delete, name="confirm_delete"),
    path("courses/destroy/<int:course_id>/confirm", views.delete_course, name="delete_course"),
    path("courses/<int:course_id>/comments", views.course_comments, name="course_comments"),
]