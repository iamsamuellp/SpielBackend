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


@api_view(['POST'])  
@permission_classes([IsAuthenticated])
def add_replys(request):
 if request.method == 'POST':
      serializer= ReplySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def edit_replys(request):



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_reply(request):
  if request.method == 'DELETE':
    serializer = ReplySerializer(data=request.data)
  if serializer.is_valid():
    serializer.delete(user=request.user) 
    return Response({'message':'the Reply was deleted succesfully '}, status=status.HTTP_204_NO_CONTENT ) 



