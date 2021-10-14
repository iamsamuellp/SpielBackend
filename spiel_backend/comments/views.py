from rest_framework import serializers, status 
from rest_framework. views import APIView
from rest_framework.response import Response 
from rest_framework. permissions import IsAuthenticated, AllowAny
from rest_framework .decorators import api_view ,permission_classes
from .models import Comment
from .serializers import CommentSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
  replys=Comment.objects.all()
  serializer = CommentSerializer(replys, many=True)
  return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_commnet(request):
  if request.method == 'POST':
      serializer= CommentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_story(request):
  if request.method == 'DELETE':
    serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.delete(user=request.user) 
    return Response({'message':'the Comment was deleted succesfully '}, status=status.HTTP_204_NO_CONTENT ) 