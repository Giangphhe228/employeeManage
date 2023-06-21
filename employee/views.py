from django.shortcuts import render
from .models import Employee
from .serializers import EmpSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

# Create your views here.
class EmpViewSet(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head']

    def get(self, request, format=None):
        # data= ['ada', 'ada/:name']
        emp = Employee.objects.all()
        serializer = EmpSerializer(emp, many=True)
        # print("den day roi")
        # return Response(dep.data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'data':serializer.data})
    