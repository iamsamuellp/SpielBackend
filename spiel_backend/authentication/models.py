from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
  # add more fields here
  is_employee = models.BooleanField(default=False)
  favorite_genre= models.CharField(max_length=150)
  favorite_type= models.CharField(max_length=150)

  def __str__(self):
    return self.username