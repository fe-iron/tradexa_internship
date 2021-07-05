from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.CharField(max_length=25)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
