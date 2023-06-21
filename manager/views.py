from django.shortcuts import render
from .models import Manager
from .serializers import ManagerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView

# Create your views here.
class ManagerViewSet(GenericAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # data= ['ada', 'ada/:name']
        Man = Manager.objects.all()
        serializer = ManagerSerializer(Man, many=True)
        # print("den day roi")
        # return Response(dep.data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'data':serializer.data})