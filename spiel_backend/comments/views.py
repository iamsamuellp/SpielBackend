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