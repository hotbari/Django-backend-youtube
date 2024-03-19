from django.test import TestCase
from django.contrib.auth import get_user_model # 유저 생성함수 import

# Create your tests here.

# TDD (User 관련 테스트 코드)
# Test Driven Development
# FASTAPI에서 개발 시간 단축에 좋음
# 테스트 코드에서 완전체를 구현하고 이 코드가 통과되기 위해서 코드를 작성하는 방식


class UserTestCase(TestCase): # 일반/슈퍼 유저생성 테스트 코드
    
    # 일반 유저 생성 테스트
    def test_create_user(self):
        email = 'sungchan@smtown.com'
        password = 'password123'
        
        user = get_user_model().objects.create_user(email=email, password=password)
        
        # 유저가 잘 만들어졌는지 확인
        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password)) # 장고에서 패스워드는 해쉬와 되니까 << 함수 이용해서 True면됨
        self.assertTrue(user.check_password(password)) # assertEqual보다 편하게
        # self.assertEqual(user.is_superuser, False) # 슈퍼유저 권한이 False인지, ELK 스택 써보세요
        self.assertFalse(user.is_superuser)
        
        
# 테스트 코드 실행하는 법 : docker-compose run -rm app sh -c 'python manage.py test users'
# 배포 후에는 로컬에서 python manage.py 하고 장고만 도커로 업데이트 하고.. 그람 됨
        
        
        
        
        
        
    
    # 슈퍼 유저 생성 테스트
    def test_create_superuser(self):
        email = 'supersungchan@smtown.com'
        password = 'password123'
        
        user = get_user_model().objects.create_superuser(email=email,password=password)
        
        # 슈퍼유저라면 이래야한다
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
        return user