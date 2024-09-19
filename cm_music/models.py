from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class ContactMessage(models.Model):
    name = models.CharField(max_length=108)
    email = models.EmailField(max_length=108)
    message = models.CharField(max_length=1008)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.name}' wrote: {self.message} - {self.timestamp.strftime('%A, %b %d, %Y at %H:%M:%S')}"

    def is_valid_message(self):
        if not self.name or not self.email or not self.message:
            return False
        return True