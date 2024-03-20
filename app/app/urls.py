"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)


urlpatterns = [
    path('admin/', admin.site.urls),
    ## drf-spectacular
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # swagger-ui : 개발자가 개발할 때 사용, 값 넣어 테스트 가능!
    # url 넘 길어서 docs로 단순하게 바꿈
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # redoc : 기획자&비개발자가 결과물 확인시 사용, API 깔끔!
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    
    # REST API
    path('api/v1/video/', include('videos.urls'))
]
