# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Formula


class ForSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    value = serializers.CharField(max_length=250)

    class Meta:
        model = Formula
        fields = ['name', 'value']
        ordering = ['-id']


