
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()
    
    class Meta:
        ordering = ["email"]
        verbose_name = "User"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)