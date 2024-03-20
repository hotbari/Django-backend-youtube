from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoSerializer(serializers.ModelSerializer):
    
    # video가 FK를 가졌을 땐 손쉽게 접근 가능하지만 자녀들이 video에 접근하려면 reverse access 기능 필요
    user = UserSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = "__all__"