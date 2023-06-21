# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=250)
    createBy = serializers.CharField(max_length=250)
    updateBy = serializers.CharField(max_length=250)
    createDate = serializers.DateTimeField()
    updateDate = serializers.DateTimeField()

    class Meta:
        model = Note
        fields = ['content', 'createBy','updateBy', 'createDate', 'updateDate']
        ordering = ['-id']


