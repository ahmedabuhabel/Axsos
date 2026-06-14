from django.urls import path
from . import views

urlpatterns = [
    path("", views.wall_index, name="wall"), 
    
    path("post_message", views.post_message, name="post_message"),
    path("post_comment/<int:message_id>", views.post_comment, name="post_comment"),
    path("delete_message/<int:message_id>", views.delete_message, name="delete_message"),
]