from django.shortcuts import render
from rest_framework.views import APIView
from .models import ChatRoom
from .serializer import ChatRoomSerializer, ChatMsgSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from django.shortcuts import get_object_or_404



''' 
ChatRoom,
(1) ChatRoomList
api/v1/chat
get - 전체 채팅방 조회 (auth로 request.user의 채팅방만 조회됨)
post - 채팅방 생성

(2) ChatRoomDetail - 이거까진 안한대용
api/v1/chat/{room_id}
put - 채팅방 이름, 인원수 제한 등 채팅방 관련 수정
delete - 채팅방 삭제

ChatMessage
(1)ChatMessageList
get - 채팅 내역 조회
post - 채팅 메세지 생성
'''

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        
        return Response(serializer.data) # 200
    
    
    def post(self, request):
        user_data = request.data # 유저가 보내준 데이터
        serializer = ChatRoomSerializer(data=user_data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()


class ChatMsgList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)
        
        serializer = ChatMsgSerializer(messages, many=True)
        return Response(serializer.data)
        
        
    def post(self, request, room_id):
        user_data = request.data
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        
        serializer = ChatRoomSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(room=chatroom, sender=request.user)
        
        return Response(serializer.data, 201)