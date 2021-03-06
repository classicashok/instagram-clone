from django.db import models
from user_app.models import UserModel
# Create your models here.
class PhotoModel(models.Model):
    caption = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    photo =models.ImageField(upload_to='profile_pic')

class CommentModel(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    parent_post = models.ForeignKey(PhotoModel, on_delete=models.CASCADE)
