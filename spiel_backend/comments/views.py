import re
from django.http import request
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
def new_comment(request):
  if request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  



@api_view(['PUT','GET','DELETE'])
@permission_classes([AllowAny])
def edit_comment(request,pk):
  if request.method == 'PUT':
    comment = Comment.objects.get(user = pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
  elif request.method == 'GET':
    comment = Comment.objects.get(user = pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data) 
  elif request.method == 'DELETE':
    cd = Comment.objects.get(id = pk)
    cd.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  