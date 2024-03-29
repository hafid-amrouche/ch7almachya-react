import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib.auth.models import User
from messaging.models import Conversation
from django.core.exceptions import ObjectDoesNotExist
from asgiref.sync import sync_to_async
from django.core.serializers.json import DjangoJSONEncoder  # Import the Django JSON Encoder
from channels.db import database_sync_to_async
from urllib.parse import parse_qs

@database_sync_to_async
def get_user(token_key):
        # Retrieve user based on the authentication token
        try:
            token = UntypedToken(token_key)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            return user 
        except (InvalidToken, TokenError, User.DoesNotExist):
            # print('Invalid token')
            return AnonymousUser()

class GeneralDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_string = self.scope.get("query_string", b"").decode("utf-8")
        query_parameters = parse_qs(query_string)
        token_key = query_parameters.get("token", [""])[0]
        user = await get_user(token_key)
        if user:
            self.room_group_name = f'general-data-{user.id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            print(f"User {user.username} connected to the websocket-General data.")
        else:
            self.disconnect()

    async def disconnect(self, close_code):
        pass
        # print('///////////// last messages General data')
    
    async def send_notification(self, event): 
        serializer_notification = event['serializer_notification']
        notification = event['notification']
        notification.is_acknowledged = True
        # Wrap the synchronous database operation using database_sync_to_async
        await database_sync_to_async(notification.save)()
        content = {
            'type': 'notification-update',
            'notification': serializer_notification,
        }
        content = json.dumps(content, cls=DjangoJSONEncoder)
        await self.send(content)
    
    async def send_conversation(self, event): 
        content = event['content']
        content = json.dumps(content , cls=DjangoJSONEncoder)
        await self.send(content)

    async def delete_notification(self, event):
        notification_id = event['notification_id']
        content={
            'type' : 'delete-notification',
            'notification-id' : notification_id
        }
        content = json.dumps(content)
        await self.send(content)

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_string = self.scope.get("query_string", b"").decode("utf-8")
        query_parameters = parse_qs(query_string)
        token_key = query_parameters.get("token", [""])[0]
        user = await get_user(token_key)
        if user :
            self.friend_id = int(query_parameters.get("friend-id", [""])[0])
            self.user_id = user.id
            self.room_group_name = f'chatroom-{min(self.user_id, self.friend_id)}-{max(self.user_id, self.friend_id)}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            self.disconnect()

    async def disconnect(self, close_code):
        pass
        # print('///////////// last messages General data')
    
    async def receive(self, text_data):
        pass

    async def send_message(self, event): 
        serializer_message = event['serializer_message']
        message = event['message']
        message.is_seen_by_receiver = True
        # Wrap the synchronous database operation using database_sync_to_async
        await database_sync_to_async(message.save)()
        content = {
            'type': 'message-update',
            'message': serializer_message,
        }
        content = json.dumps(content, cls=DjangoJSONEncoder)
        await self.send(content)
    