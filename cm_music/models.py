from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=108)
    email = models.CharField(max_length=108)
    message = models.CharField(max_length=1008)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.name}' wrote: {self.message} - {self.timestamp.strftime('%A, %b %d, %Y at %H:%M:%S')}"
