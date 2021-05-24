from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


# Create your models here.
class Post(Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post Title:- {title}".format(title = self.title)
   

class PostLikes(Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Likes for {post}".format(post = self.post)
