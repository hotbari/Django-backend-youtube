from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SubSerializer
from rest_framework.response import Response
from .models import Subscription
from rest_framework import status

# request.user 나 기준
class SubscriptionList(APIView):
    
    # get 으로 내 구독 리스트 조회
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)

    
    # 구독하기
    def post(self, request):
        user_data = request.data # 유저 데이터 불러옴
        serializer = SubSerializer(data=user_data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        
        return Response(serializer.data, 201)
        



# api/v1/subscription/{user_id}
class SubscriptionDetail(APIView):
    # 특정 유저의 구독자 리스트 조회
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk)
        serializer = SubSerializer(subs, many=True)
        
        return Response(serializer.data) # 그냥 내리면 200
    
    
    # 구독 취소
    def delete(self, request, pk):
        from django.shortcuts import get_object_or_404
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user) # 아무나 삭제할 수 없게 ..
        sub.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)