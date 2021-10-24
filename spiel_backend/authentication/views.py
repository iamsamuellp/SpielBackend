from django.shortcuts import render

import authentication
# from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
User = get_user_model()
# Create your views here.

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegistrationSerializer


class UserView(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise HTTP_404_NOT_FOUND
    
    def get(self,request,pk):
        comment = self.get_object(pk)
        serializer = RegistrationSerializer(comment)
        return Response(serializer.data)

    # def get(self,request,pk):
    #     storytype = self.get_object(pk)
    #     serializer = RegistrationSerializer(storytype)
    #     return Response(serializer.data)    