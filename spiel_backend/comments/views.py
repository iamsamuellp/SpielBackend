import re
from rest_framework import serializers, status 
from rest_framework. views import APIView
from rest_framework.response import Response 
from rest_framework. permissions import IsAuthenticated, AllowAny
from rest_framework .decorators import api_view ,permission_classes

import comments
from .models import Comment
from .serializers import CommentSerializer
from django.http.response import Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
  comments=Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def new_commnet(request):
  if request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_story(request):
  if request.method == 'DELETE':
    serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.delete(story=request.story) 
    return Response({'message':'the Comment was deleted succesfully '}, status=status.HTTP_204_NO_CONTENT ) 