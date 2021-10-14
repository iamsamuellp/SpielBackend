from django.core.checks import messages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes

from comments import serializers
import story_submission
from .models import StorySubmission
from .serializers import StorySerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_stories(requset):
    stories = StorySubmission.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_story(request):
  if request.method == 'POST':
      serializer= StorySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_story(request):
  if request.method == 'DELETE':
    serializer = StorySerializer(data=request.data)
  if serializer.is_valid():
    serializer.delete(user=request.user) 
    return Response({'message':'the Story was deleted succesfully '}, status=status.HTTP_204_NO_CONTENT ) 
