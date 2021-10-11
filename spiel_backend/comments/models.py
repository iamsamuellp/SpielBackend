from django.db import models
from story_submission.models import StorySubmission 


class Comment(models.Model):
  story = models.ForeignKey(StorySubmission,on_delete=models.CASCADE) 
  comment = models.CharField(max_length=1000)
  likes = models.IntegerField(null=0)
  dislikes = models.IntegerField(null=0)
