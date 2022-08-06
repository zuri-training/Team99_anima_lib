from django.db import models

from apps.accounts.models import CustomUser

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Pubish")
)

class Post(models.Model):
    title = models.CharField(max_length=70,null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="post_author")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length= 3000,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS, default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    #comment_user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=70,null=False)
    email = models.TextField(max_length= 3000,null=False)
    content = models.TextField(max_length= 3000,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title