from django.db import models

from apps.accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70,null=False)
    content = models.TextField(max_length= 3000,null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="post_author")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    comment = models.TextField(max_length= 500,null=False)
    comment_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comment_author")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_author")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title