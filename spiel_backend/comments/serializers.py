from django.db import models
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'comment', 'likes', 'dislikes', 'storysubmission_id',]