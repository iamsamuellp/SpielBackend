from django.db import models
from comments.models import Comment



class Reply(models.Model):
  comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
  reply= models.CharField(max_length=1000)
  likes = models.IntegerField(null=0)
  dislikes = models.IntegerField(null=0)