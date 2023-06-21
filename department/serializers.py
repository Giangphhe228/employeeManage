# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Department


class DepSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    createBy = serializers.CharField(max_length=250)
    updateBy = serializers.CharField(max_length=250)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()
    users_id = serializers.CharField(max_length=250)

    class Meta:
        model = Department
        fields = ['name', 'createBy', 'updateBy', 'createAt', 'updateAt','users_id']
        ordering = ['-id']


