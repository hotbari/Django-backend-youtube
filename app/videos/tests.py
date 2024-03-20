## TDD 

# from django.test import TestCase # API 테스트할거라 없앰

# drf에서 Import
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.

class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 동작하는 함수
    # 데이터를 만들어줘야한다 테스트코드가 동작할 때는 DB 비어있음
    # 유저 생성/로그인 -> 비디오 생성
    def setUp(self):
        # ORM 방식
        # self.__으로 하면 클래스 변수에 등록되서 동일클래스 다른 함수에서도 사용할 수 있음!!!!
        self.user = User.objects.create_user(
            email='sungchan@smtown.com',
            password='password123'
        )
        
        # 로그인 시키기
        self.client.login(email='sungchan@smtown.com',password='password123')
        
        # 비디오 생성
        self.video = Video.objects.create(
            title = 'test video',
            link = 'http://www.test.com',
            user = self.user
        )
        
    
    # 127.0.0.1:8000/api/v1/video
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v1/video' 이렇게하면 유지보수 구림
        url = reverse('video-list') # 이름으로 urls.py 에서 가져옴
        res = self.client.get(url) # 전체 비디오 조회 데이터가 들어있음
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json') # 제이슨 형태로 들어옴?
        self.assertTrue(len(res.data) > 0) # 데이터 개수 0보다 큼?
        
        for video in res.data:
            self.assertIn('title', video) # 응답데이터에 title 있음?
        
    def test_video_list_post(self):
        url = reverse('video-list') # api/v1/video 들어옴
        data = {
            'title' : 'test video post',
            'link' : 'http://test.com',
            'category' : 'test category',
            'thumbnail' : 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4',b'file_content', 'video/mp4'),
            'user' : self.user.pk
        }
        
        self.client.login(email='sungchan@smtown.com', password='password123')
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video post')
        
    ## api/v1/video/{pk} -> REST API
    # 특정 비디오 조회 
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk}) # urls.py에 작성한 경로를 가져온다
        
        # 항상 서버를 요청하면 응답이 온다! res = ...
        res = self.client.get(url)
        
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    # 특정 비디오 업데이트
    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        data = {
            'title' : 'test video update',
            'link' : 'http://test.com',
            'category' : 'test category',
            'thumbnail' : 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4',b'file_content', 'video/mp4'),
            'user' : self.user.pk
        }
        res = self.client.put(url,data)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'],'test video update')
    
    # 특정 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        
        res = self.client.delete(url)
        
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT) # 204
        
        # 진짜... 지워졌을까? 
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)