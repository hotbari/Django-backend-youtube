from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# Create your models here.
class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    
    # User:Comment = 1:N N이 FK 갖는다
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    
    