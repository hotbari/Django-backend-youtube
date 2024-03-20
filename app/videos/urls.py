from django.urls import path
from .views import VideoList, VideoDetail

# api/v1/video
urlpatterns = [
    path('', VideoList.as_view(),name='video-list'),
    # api/v1/video/{pk}
    # url만들 때 끝에 / 붙여주는 습관 들이기!
    path('<int:pk>/', VideoDetail.as_view(),name='video-detail')
]
