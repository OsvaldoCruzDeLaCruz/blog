from dataclasses import field
from .models import *
from rest_framework import serializers

class CetegorySerializer(serializers.ModelSerializer):
    thumbnail=serializers.CharField(source='get_thumbail')
    class Meta:
        model = Category
        fields=[
            'id',
            'name',
            'thumbnail',
        ]
