from django.db import models
from common.models import CommonModel


# 모델 쪼개서 만들꺼에요 뿎뿌꾸ㅜ
# 왜 쪼개요?
# 채팅방을 구분하면 관리가 편하고요 (모델 구분)
# 확장성(오픈 채팅, 업무채팅 등) 좋아요
# 예) 업무채팅방은 비번 치고 들어가야되는데 그런걸 메세지 클래스에서 관리하기 어렵겠죵

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 데이터는 남기고 sender(User)를 null로 두겠습니다~
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    msg = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)    