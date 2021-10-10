from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


class Story_Submission(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title= models.CharField(max_length=150)
  author=models.CharField(max_length=100)
  story=models.CharField(max_length=7500)
  genre=models.CharField(max_length=200)
  story_type=models.CharField(max_length=100)