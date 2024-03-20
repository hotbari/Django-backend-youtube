from django.db import models
from common.models import CommonModel
from users.models import User
# Create your models here.

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 버킷에 파일을 저장하면 만들어지는 URL을 저장하는것 (부하 분산)
    video_file = models.FileField(upload_to='storage/')
    
    # User:Video = 1:N Video가 FK를 갖는다
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    