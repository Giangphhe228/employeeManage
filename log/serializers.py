# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    note = serializers.CharField(max_length=250)
    createBy = serializers.CharField(max_length=250)
    updateBy = serializers.CharField(max_length=250)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()
    okrs_id = serializers.CharField(max_length=250)

    class Meta:
        model = Log
        fields = ['note', 'createBy','updateBy', 'createAt', 'updateAt','okrs_id']
        ordering = ['-id']


