from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
     author_name = models.CharField(max_length=255)
     author_image = models.ImageField(upload_to="Author", null=True, blank=True)
     title = models.CharField(max_length=255, unique=True) 
     coverImage = models.ImageField(upload_to='static/Blog')
     description = models.TextField()
     total_likes = models.PositiveBigIntegerField(default=0, null=True, blank=True)
     totalComments = models.PositiveBigIntegerField(default=0)
     createdAt = models.DateTimeField(auto_now_add=True)
     likes = models.ManyToManyField(User)

     def __str__(self):
          return f'{self.title} :: {self.id}'


class Comment(models.Model):
     author = models.CharField(max_length=255)
     comments = models.TextField()
     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
     totalReplies = models.PositiveBigIntegerField(default=0)
     createdAt = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return f'::: {self.author} ::: {self.id}'



class Reply(models.Model):
     author = models.CharField(max_length=255)
     reply = models.TextField()
     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
     createdAt = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return f'Reply: {self.author}  ------ ::: {self.comment.id} '
     
     