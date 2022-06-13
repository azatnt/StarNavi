from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_request = models.DateTimeField(null=True, blank=True)



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=250)
    description = models.TextField()
    likes = models.ManyToManyField(User, through='PostLikes', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        db_table = 'post_likes'
