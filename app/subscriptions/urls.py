from django.urls import path
from . import views

urlpatterns = [
    path('',views.SubscriptionList.as_view(), name='sub-list'), # api/v1/sub, 테스트에서 name 정해줌
    path('<int:pk>', views.SubscriptionDetail.as_view(), name='sub-detail')
]