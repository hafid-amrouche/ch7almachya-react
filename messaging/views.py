import time
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Message, Conversation
from user.models import User
from .serializers import MessageSerializer, ConversationSerializer
import json
from django.db.models import Q
from user.update_user_realtime_data import update_conversation
from django.utils.translation import gettext as _


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    try:
        user = request.user
        friend = User.objects.get(id=request.POST.get('friend_id'))
        text = request.POST.get('text').strip()
        if text:
            message = Message.objects.create(
                sender = user,
                receiver = friend,
                text = text
            )
            conversation = Conversation.objects.filter(Q(user1=user, user2=friend) | Q(user1=friend, user2=user)).first()
            if conversation == None :
                conversation = Conversation.objects.create(user1=user, user2=friend)
            conversation.last_message = message
            conversation.save()

            # send new conversation to user
            serializer_conversation = ConversationSerializer(conversation, many=False, context={'user' : friend}).data
            update_conversation(friend.id, serializer_conversation)
            if friend != user:
                serializer_conversation = ConversationSerializer(conversation, many=False, context={'user' : user}).data
                update_conversation(user.id, serializer_conversation)
            #################################
            return JsonResponse({'detail' : 'Sent'}, status=200)
        else:
            return JsonResponse({'detail' : 'Message cannot be empty'}, status=400) 
    except Exception as e:
        try:
            message.delete()
        except:
            pass
        raise
        return JsonResponse({'detail' : str(e)}, status=400)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    user = request.user
    friend = User.objects.get(id=request.POST.get('friend-id'))
    seen_messages = json.loads(request.POST.get('seen-messages'))
    try:
        messages = Message.objects.exclude(id__in = seen_messages).filter(Q(sender=user, receiver=friend) | Q(sender=friend, receiver=user))
        messages.filter(receiver=user).update(is_seen_by_receiver=True)
        cond = messages.count() > 20
        messages = messages[:20]
        messages = MessageSerializer(messages, many=True).data
        response = [messages, cond]
        if seen_messages == []:
            response.append({
                'friend_name': {'text' :friend.page.name, 'is_verified': friend.page.is_verified } if friend.extention.is_page else friend.get_full_name(),
                'friend_username' : friend.username,
                'friend_image': friend.extention.image_150
            })
        return Response(response)
    except Exception as e:

        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_conversations(request):
    seen_conversations = json.loads(request.POST.get('seen-conversations'))
    try:
        conversations = Conversation.objects.filter(Q(user1 = request.user )| Q(user2 = request.user)).exclude(id__in=seen_conversations)
        cond = conversations.count() > 20
        conversations.update(is_acknowledged=True)
        conversations = conversations[:20]
        conversations = ConversationSerializer(conversations, many=True, context={'user' : request.user}).data
        return Response([conversations, cond])
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)