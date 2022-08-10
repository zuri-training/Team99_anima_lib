from tkinter import N
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    username=None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    name = models.CharField(max_length=200, db_index=True, blank=True)
    github_url = models.URLField(max_length=255, blank=True)
    project_url = models.URLField(max_length=255, blank=True)
    twitter_url = models.URLField(max_length=255, blank=True)
    image = CloudinaryField('image', null=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()
    
    class Meta:
        ordering = ["email"]
        verbose_name = "User"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)