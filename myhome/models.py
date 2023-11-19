from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20,)
    image = models.CharField( max_length=300,blank=True, null=True)
    author = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=1000)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
class Resgister(models.Model):
    user = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    def __str__(self):
        return f"{self.author.username}\'s Post - {self.title}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def Count_like(self):
        return self.like.count()
    def get_absolute_url(self):
        return reversed('post_detail',kwargs={'pk':self.pk})
    

