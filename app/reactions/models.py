from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q


class Reaction(CommonModel):
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # circular error 방지
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    
    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0
    
    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Disllike'),
        (NO_REACTION, 'No Reaction')
    )
    
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )
    
    # 다른 모델에서도 좋/싫 확인하기 위해
    # 리액션 테이블에서 비디오를 기준으로 좋/싫 개수를 알려준다
    # 와 이거는 이해가 잘 안가묘
    # 이거 비디오에서 보여주고 싶으니께 비디오 시리얼라이저 ㄱㄱ
    # 한 번만 하는거 어케 하지
    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk',filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk',filter=Q(reaction=Reaction.DISLIKE)),
        )
        
        return reactions