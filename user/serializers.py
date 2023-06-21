# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    employeeCode = models.CharField(max_length=250)
    fullName = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    birthDate = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=250)
    emailAddress = models.CharField(max_length=250)
    jobCode = models.CharField(max_length=250)
    jobTitle = models.CharField(max_length=250)
    officerTitle = models.CharField(max_length=250)
    locationAddress = models.CharField(max_length=250)
    organizationNamePath = models.CharField(max_length=250)
    organizationCodePath = models.CharField(max_length=250)
    createAt = models.DateTimeField(max_length=250)
    updateAt = models.DateTimeField(max_length=250)
    level= models.CharField(max_length=250)
    dateIn = models.DateTimeField(max_length=250)
    dateOut = models.DateTimeField(max_length=250)

    class Meta:
        model = User
        fields = ['employeeCode', 'fullName', 'gender', 'birthDate', 'phoneNumber', 'emailAddress', 'jobCode', 'jobTitle', 'officerTitle',
                   'locationAddress', 'organizationNamePath', 'organizationCodePath', 'createAt', 'updateAt', 'level', 'dateIn', 'dateOut']
        ordering = ['-id']


