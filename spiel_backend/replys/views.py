from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Reply
from .serializers import ReplySerializer


@api_view(['GET'])  
@permission_classes([AllowAny])
def get_all_replys(request):
  reply = Reply.objects.all()
  serializer = ReplySerializer(reply,many=True)
  return Response(serializers.data)
