from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView

# Create your views here.
class UserViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # data= ['ada', 'ada/:name']
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # print("den day roi")
        # return Response(dep.data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'data':serializer.data})