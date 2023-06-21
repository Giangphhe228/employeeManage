# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Source


class SourceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    value = serializers.CharField(max_length=250)

    class Meta:
        model = Source
        fields = ['name', 'value']
        ordering = ['-id']


