from django.db import models

# Create your models here.
# 가장 기본적인 모델 클래스 상속 : class Meta 같은 기능을 사용할 수 있다
class CommonModel(models.Model):
    # 왜 데이트타임필드로 했어요? 용량을 그렇게 크게 잡아먹지 않고 시간데이터가 비교적 더 중요하다고 느껴서
    created_at = models.DateTimeField(auto_now_add=True) # 최초 1회만
    updated_at = models.DateTimeField(auto_now=True) # 계속 바뀜
    
    class Meta:
        abstract = True # DB에 테이블을 추가하지 마시오.