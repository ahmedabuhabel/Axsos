from django.db import models
from login_register_app.models import User
from django.utils import timezone
from datetime import timedelta

class MessageManager(models.Manager):
    def message_validator(self, post_data):
        errors = {}
        if len(post_data.get('message', '').strip()) < 1:
            errors['message'] = "Message content cannot be empty."
        return errors

class CommentManager(models.Manager):
    def comment_validator(self, post_data):
        errors = {}
        if len(post_data.get('comment', '').strip()) < 1:
            errors['comment'] = "Comment content cannot be empty."
        return errors

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = MessageManager()

    def can_be_deleted(self):
        return timezone.now() < self.created_at + timedelta(minutes=30)

class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CommentManager()