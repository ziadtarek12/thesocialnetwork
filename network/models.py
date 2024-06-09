from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Post(models.Model):
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp =models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    likes = models.ManyToManyField(User, related_name="user_likes", blank=True)

class Likes(models.Model):
    pass
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followings")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followers")

    class Meta:
        unique_together = ['following', 'follower']
