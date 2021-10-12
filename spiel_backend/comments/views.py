from rest_framework import serializers, status 
from rest_framework. views import APIView
from rest_framework.response import Response 
from rest_framework. permissions import IsAuthenticated, AllowAny
from rest_framework .decorators import api_view ,permission_classes
from .models import Comment
from .serializers import CommentSerializer

class CommentList(APIView):

  permission_classes = [AllowAny]

def get(self,request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializers.data)
  