from django.db import models
import re
from datetime import datetime, date
# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        first_name = post_data.get('first_name', '').strip()
        last_name = post_data.get('last_name', '').strip()
        email = post_data.get('email', '').strip()
        password = post_data.get('password', '')
        confirm_password = post_data.get('confirm_password', '')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        birthday_str = post_data.get('birthday', '').strip()
        if len(first_name) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(last_name) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email format (e.g., example@domain.com)."
        elif self.filter(email=email).exists(): 
            errors['email'] = "This email is already registered!"
        if len(password) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if  password != confirm_password:
            errors['confirm_password'] = "Passwords do not match"
        if not birthday_str:
            errors['birthday'] = "Birthday field is required"
        else:
            try:
                birthday_date = datetime.strptime(birthday_str, '%Y-%m-%d').date()
                today = date.today()
                
                # أ) التأكد أن التاريخ في الماضي (Ninja Bonus)
                if birthday_date >= today:
                    errors['birthday'] = "Birthday must be in the past"
                else:
                  
                    age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
                    
                    if age < 13:
                        errors['birthday'] = "You must be at least 13 years old to register"
            except ValueError:
                errors['birthday'] = "Invalid date format"
        return errors
    def login_validator(self, post_data):
        errors = {}
        password = post_data.get('password', '')
        email = post_data.get('email', '').strip()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email format (e.g., example@domain.com)."
        if len(password) < 8:
            errors['password'] = "Password should be at least 8 characters"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
  