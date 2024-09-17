from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Post(models.Model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sender_posts")
    content = models.CharField(max_length=108)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.sender}' wrote: {self.content} - {self.timestamp.strftime('%A, %b %d, %Y at %H:%M:%S')}"
