from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Model for User
class User(AbstractUser, models.Model):
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/')
    name = models.TextField(max_length=64)
    bio = models.TextField(max_length=64, null=True)

# Model for Comment
class Comment(models.Model):
    writer = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    description = models.TextField(max_length=64)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

# Model for Post
class Post(models.Model):
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=64)
    comment = models.ForeignKey(Comment, related_name="post", on_delete=models.CASCADE)
    react = models.IntegerField(default=0)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

# Model for Reactor
class Reactor(models.Model):
    reactor = models.ForeignKey(User, related_name="react_post", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="react_person", on_delete=models.CASCADE)
