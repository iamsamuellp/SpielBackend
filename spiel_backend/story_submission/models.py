from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime



class StorySubmission(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title= models.CharField(max_length=150)
  author=models.CharField(max_length=100)
  story=models.CharField(max_length=7500)
  genre=models.CharField(max_length=200)
  story_type=models.CharField(max_length=100)
  approved_story = models.BooleanField(default=False)
  published_date=models.DateField( verbose_name=("Creation date"), 
  auto_now_add=True, null=True)