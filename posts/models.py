from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    """
    Represents a post made by the user
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_vm4gvx', blank=True
    )
    location = models.CharField(max_length=150, default="Somewhere")
    country = models.CharField(max_length=150, default="Unknown")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
