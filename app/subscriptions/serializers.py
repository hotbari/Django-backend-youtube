from rest_framework import serializers
from .models import Subscription

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        
    # 내가 나를 구독할 수 있나요? ㄴㄴ
    # 이걸 뷰에서 해주면 매번 검증을 해줘야함
    # validate는 모델 시리얼라이즈에 포함된 함수임
    # 셀프 구독하면 에러메세지 발생
    # data는 딕셔너리 타입
    # 프론트에서 셀프 구독 못하게 막아놔야해유
    def validate(self, data):
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError("You can't subscribe to yourself")
        
        return data