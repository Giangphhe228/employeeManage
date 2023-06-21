from django.shortcuts import render
from .models import Formula
from .serializers import ForSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

# Create your views here.
class DepartViewSet(APIView):
    queryset = Formula.objects.all()
    serializer_class = ForSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head']

    def get(self, request, format=None):
        # data= ['ada', 'ada/:name']
        dep = Formula.objects.all()
        serializer = ForSerializer(dep, many=True)
        # print("den day roi")
        # return Response(dep.data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'data':serializer.data})
    