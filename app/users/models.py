from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)

class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, password):
        # 이메일이 비어있을 때
        if not email:
            raise ValueError("Email!")
        
        user = self.model(email=email)
        user.set_password(password) # user가 보낸 패스워드 해쉬화
        user.save(using=self._db) # 내가 지금 사용하는 db에 저장한다 (언더바는 뭐임?
        
        return user
    
    # 슈퍼 유저 생성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
        


class User(AbstractBaseUser,PermissionsMixin,UserManager):
    email = models.CharField(max_length=255, unique=True) # 이거 왜 emailfield로 안함? 해도 된대여; 차이가 모임요
    nickname = models.CharField(max_length=255) 
    is_bussiness = models.BooleanField(default=False)
    # email = models.EmailField()
    
    # PermissionsMixin으로 커스텀해서 권한 관리
    is_active = models.BooleanField(default=True) # 유저를 활성화 시키고
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email' # createsupersuser에 필요한 email, usernmae, password에서 username은 필수 입력이라 유저 정보에 필수로 들어가는 이메일을 username으로 해줌
    
    objects = UserManager() # 유저 생성 및 관리 : 유저를 구분해서 관리해야죵! (일반 유저 - 관리자 유저)
    
    def __str__(self):
        return f'email: {self.email}, nickname: {self.nickname}'
    
    
