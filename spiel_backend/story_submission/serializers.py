from rest_framework import serializers
from .models import StorySubmission

class StorySerializer(serializers.ModelSerializer):
  class Meta:
    model= StorySubmission
    fields =['id', 'title', 'author','story','genre','user_id','approved_story','published_date','story_type']