from django.db import models

# Create your models here.
class Adduser(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=500, default=None)

    def __str__(self):
        return f"{self.email}"
