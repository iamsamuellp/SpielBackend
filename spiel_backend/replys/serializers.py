from django.db import models
from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):

  class Meta:
    model = Reply
    fields = ['id','reply','likes','dislikes','comment_id']