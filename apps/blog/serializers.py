from dataclasses import field
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    thumbail=serializers.CharField(source="get_thumbnail")
    video = serializers.CharField(source = "get_video")
    
    class Meta:
        model = Post
        fields=[
            'blog_uuid',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'category',
            'author',
            'published',
            'status',
        ]
