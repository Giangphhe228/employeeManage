# from typing_extensions import Required
from rest_framework import serializers
from .models import Permission


class PerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    createBy = serializers.CharField(max_length=250)
    updateBy = serializers.CharField(max_length=250)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()

    class Meta:
        model = Permission
        fields = ['name', 'createBy','updateBy', 'createAt', 'updateAt']
        ordering = ['-id']


