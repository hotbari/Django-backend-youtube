from django.test import TestCase
from .models import Subscription
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse
import pdb

class SubscriptionTestCase(APITestCase):
    # 테스트 코드 실행 시, 가장 먼저 실행되는 함수
    # 데이터 생성
    # 구독할-구독될 유저 데이터 2개 생성, 1명의 유저 로그인
    def setUp(self):
        self.user1 = User.objects.create_user(email='anthon@smtown.com', password='password123')
        self.user2 = User.objects.create_user(email='wonbin@smtown.com', password='password123')
        
        self.client.login(email='anthon@smtown.com', password='password123')
        
    def test_sub_list_get(self):
        Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2) # 구독
        
        url = reverse('sub-list')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data),1)
        
        self.assertEqual(res.data[0]['subscribed_to'], self.user2.id)
        
        
    
    # 구독 버튼 테스트
    # api/v1/sub
    def test_sub_list_post(self):
        url = reverse('sub-list')
        data = {
            'subscriber' : self.user1.pk,
            'subscribed_to' : self.user2.pk
        }
        
        res = self.client.post(url,data)
        
        
        self.assertEqual(res.status_code, 201) # CREATED
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2) # 지금은 데이터가 하나라 get()만 해도 된다네.. 뭐지
        #self.assertTrue(len(res.data) > 0) 이거는 하면 오류나네 왜징
        
    
    # 특정 유저의 구독자 리스트
    # api/v1/sub/{user_id}
    def test_sub_detail_get(self):
        # 유저1로 유저2 구독
        Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        # 'pk'는 설정하기 나름 api/v1/sub/{user_id} 하면 다름
        url = reverse('sub-detail', kwargs={'pk':self.user2.pk})
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1) # 2번 유저를 구독한 구독자 수가 1이면 됨
        
    
    # 구독 취소
    def test_sub_detail_delete(self):
        sub = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse('sub-detail', kwargs={'pk':sub.id})
        res = self.client.delete(url)
        
        self.assertEqual(res.status_code, 204) # No Content
        #self.assertEqual(len(res.data), 0)
        self.assertEqual(Subscription.objects.count(), 0)