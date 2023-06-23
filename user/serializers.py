# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    employeeCode = serializers.CharField(max_length=250)
    fullName = serializers.CharField(max_length=250)
    gender = serializers.CharField(max_length=250)
    birthDate = serializers.CharField(max_length=250)
    phoneNumber = serializers.CharField(max_length=250)
    emailAddress = serializers.CharField(max_length=250)
    jobCode = serializers.CharField(max_length=250)
    jobTitle = serializers.CharField(max_length=250)
    officerTitle = serializers.CharField(max_length=250)
    locationAddress = serializers.CharField(max_length=250)
    organizationNamePath = serializers.CharField(max_length=250)
    organizationCodePath = serializers.CharField(max_length=250)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()
    level= serializers.CharField(max_length=250)
    dateIn = serializers.DateTimeField()
    dateOut = serializers.DateTimeField()
    okrs_id = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ['employeeCode', 'fullName', 'gender', 'birthDate', 'phoneNumber', 'emailAddress', 'jobCode', 'jobTitle', 'officerTitle',
                   'locationAddress', 'organizationNamePath', 'organizationCodePath', 'createAt', 'updateAt', 'level', 'dateIn', 'dateOut', 'okrs_id']
        ordering = ['-id']


