from django.db import models
from datetime import datetime, date
# Create your models here.
class ShowsManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
       
        title=post_data['title'].strip()
        network=post_data['network'].strip()
        description=post_data['description'].strip()
        date_str=post_data['release_date'].strip()
        converted_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if len(title) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(network) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(description) > 0 and len(description) < 10:
            errors['description'] = "Description should be at least 10 characters"
                
        if converted_date >= date.today():
                    errors['release_date'] = "Release date must be in the past"
        existing_show = Shows.objects.filter(title=title)
        if len(existing_show) > 0:
            errors['title'] = "Title already exists"
        return errors
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()

    def __str__(self):
        return {
            "title": self.title,
            "network": self.network,
            "release_date": self.release_date,
            "description": self.description,
        }
