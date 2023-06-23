# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Okr


class OkrSerializer(serializers.ModelSerializer):
    objectiveId = serializers.IntegerField()
    objectiveName = serializers.IntegerField()
    keyResultId = serializers.IntegerField()
    keyResultName = serializers.IntegerField()

    title = serializers.CharField(max_length=250)
    formula_id = serializers.CharField(max_length=250)
    source_id = serializers.CharField(max_length=250)
    type = serializers.CharField(max_length=250)
    regularly = serializers.CharField(max_length=250)
    unit = serializers.CharField(max_length=250)
    condition = serializers.IntegerField()
    norm = serializers.IntegerField()
    weight = serializers.IntegerField()
    result = serializers.IntegerField()
    ratio = serializers.IntegerField()
    note_id = serializers.CharField(max_length=250)
    status = serializers.CharField(max_length=250)
    createBy= serializers.CharField(max_length=250)
    updateBy = serializers.CharField(max_length=250)
    createAt = serializers.DateTimeField()
    updateAt = serializers.DateTimeField()
    deadline = serializers.DateTimeField()
    files = serializers.ArrayField()
    
    class Meta:
        model = Okr
        fields = ['objectiveId',
                   'objectiveName', 
                   'keyResultId',
                   'keyResultName', 
                   'title', 
                   'formula_id', 
                   'source_id', 
                   'type', 
                   'regularly',
                   'unit', 
                   'condition', 
                   'norm', 
                   'weight', 
                   'updateAt', 
                   'result', 
                   'ratio', 
                   'note_id', 
                   'status',
                   'createBy', 
                   'updateBy', 
                   'createAt', 
                   'updateAt', 
                   'deadline']
        ordering = ['-id']


