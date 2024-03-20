from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all() # QuerySet[Video1, Video2, .....]
        # 시리얼라이저 (Object->Json), 직렬화&원하는 데이터만 내려주는 기능도 있다
        
        serializer = VideoSerializer(videos, many=True) # 비디오가 여러개니까용
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        user_data = request.data
        # 역직렬화
        serializer = VideoSerializer(data=user_data)
        
        # 두 개는 셋뚜
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 데이터를 만든거라 201
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
from rest_framework.exceptions import NotFound
# 특정 비디오 조회
class VideoDetail(APIView):
    def get(self, request, pk): #api/v1/video/{pk(나는 video_id로함..)}
        try :
            video_obj = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
        
        serializer = VideoSerializer(video_obj)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        user_data = request.data
            
        serializer = VideoSerializer(video_obj, user_data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    
    def delete(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)