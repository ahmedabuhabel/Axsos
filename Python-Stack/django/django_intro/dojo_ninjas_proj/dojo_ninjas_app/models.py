from django.db import models


class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __str__(self):
        return f"{self.name} {self.city} {self.state} {self.desc}"


class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, on_delete=models.CASCADE, related_name="ninjas")

    def __str__(self):
        return f" {self.first_name} {self.last_name} {self.dojo}"
