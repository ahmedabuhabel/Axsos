from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "title": self.title,
            "network": self.network,
            "release_date": self.release_date,
            "description": self.description,
        }
