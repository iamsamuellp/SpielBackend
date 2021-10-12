from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import StorySubmission
from .serializers import StorySerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class StoryList(APIView):

  permission_classes=[AllowAny]
  
  def get(self, requset):
    stories = StorySubmission.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)