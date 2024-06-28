from django.db import models
from django.contrib.auth.forms import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=True, null=True)
     username = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     userImage = CloudinaryField('image', folder='grandeur_blog/Users_Profile_Image', blank=True, null=True)

     def __str__(self):
          return f'{self.username}, {self.userImage}'