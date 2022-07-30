from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    github_url = models.URLField(max_length=255, blank=True)
    project_url = models.URLField(max_length=255, blank=True)
    twitter_url = models.URLField(max_length=255, blank=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()
    
    class Meta:
        ordering = ["email"]
        verbose_name = "User"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)