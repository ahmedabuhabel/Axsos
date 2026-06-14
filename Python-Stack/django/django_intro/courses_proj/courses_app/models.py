from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        name = post_data.get('name', '').strip()
        description = post_data.get('description', '').strip()

        if len(name) <= 5:
            errors['name'] = "Course name must be more than 5 characters long."
        if len(description) <= 15:
            errors['description'] = "Description must be more than 15 characters long."
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)