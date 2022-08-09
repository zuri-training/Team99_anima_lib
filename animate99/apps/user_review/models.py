from django.db import models
from django.utils import timezone
from apps.accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


        
        
class Animation(models.Model):
    name = models.CharField(max_length=70, null=False)
    favourites = models.ManyToManyField(CustomUser, blank=True, related_name='favourite')
    created_on = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self):
        return self.name 