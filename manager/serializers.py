# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    department_id = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=250)
    position= serializers.CharField(max_length=50)

    class Meta:
        model = Manager
        fields = "__all__"


