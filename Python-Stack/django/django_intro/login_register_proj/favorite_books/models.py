from django.db import models
from login_register_app.models import User 

class BookManager(models.Manager):
    def book_validator(self, post_data):
        errors = {}
        title = post_data.get('title', '').strip()
        desc = post_data.get('desc', '').strip()
        
        if not title:
            errors['title'] = "Book title is required."
        if len(desc) < 5:
            errors['desc'] = "Description must be at least 5 characters long."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = BookManager()

    def __str__(self):
        return self.title