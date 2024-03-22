# videos/serializers.py

from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
#from subcriptions.serializers import SubscriptionSerializer

class VideoListSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    # 리스트에서는 댓글안보이게 지웠어요 
    
    class Meta:
        model = Video
        fields = "__all__"
        
    
    
from reactions.models import Reaction    
## 댓글이 비디오디테일 주소로 들어갈 때 보이면 좋겠어서 이러는 중 -> 시리얼라이저를 두 개로 만들어서 뷰에 구분해서 적용    
class VideoDetailSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    
    # video가 FK를 가졌을 땐 손쉽게 접근 가능하지만 
    # 자녀들이 video(부모)에 접근하려면 reverse access 기능 필요
    # _set 을 붙여야댐
    comment_set = CommentSerializer(many=True,read_only=True)
    # subscription_set = SubscriptionSerializer(many=True, read_only=True)
    
    ## ?? 이거 뭐임
    reactions = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = "__all__"
        
    
    def get_reactions(self, video):
        return Reaction.get_video_reaction(video)