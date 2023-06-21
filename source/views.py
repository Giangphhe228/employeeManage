from django.shortcuts import render
from .models import Source
from .serializers import SourceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

# Create your views here.
class SourceViewSet(APIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head']

    def get(self, request, format=None):
        # data= ['ada', 'ada/:name']
        dep = Source.objects.all()
        serializer = SourceSerializer(dep, many=True)
        # print("den day roi")
        # return Response(dep.data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'data':serializer.data})
    