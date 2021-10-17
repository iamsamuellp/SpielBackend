import re
from django.core.checks import messages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
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

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_single_stories(request,pk):
#     story = StorySubmission.objects.get(pk=pk)
#     serializer = StorySerializer(story)
#     return Response(serializer.data)
  
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def edit_story (request):  
#     story = StorySubmission


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def story_detail(request, pk):
    try: 
        story = StorySubmission.objects.get(pk=pk) 
    except StorySubmission.DoesNotExist: 
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = StorySerializer(story) 
        return Response(serializer.data) 
 
    elif request.method == 'PUT': 
        story_data = StorySubmission.objects.get(pk=pk) 
        serializer = StorySerializer(story, data=story_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        story.delete() 
        return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET'])
@permission_classes([AllowAny])
def get_published_list(request):
    story = StorySubmission.objects.filter(approved_story=True)
    if request.method=='GET':
      serializer = StorySerializer(story, many=True)
      return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_unpublished_list(request):
    story = StorySubmission.objects.filter(approved_story=False)
    if request.method=='GET':
      serializer = StorySerializer(story, many=True)
      return Response(serializer.data) 


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_story(request):
  if request.method == 'POST':
      serializer= StorySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_story(request):
  if request.method == 'DELETE':
    serializer = StorySerializer(data=request.data)
  if serializer.is_valid():
    serializer.delete(user=request.user) 
    return Response({'message':'the Story was deleted succesfully '}, status=status.HTTP_201_CREATED ) 
