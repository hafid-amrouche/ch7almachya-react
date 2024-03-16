from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from others.serializers import NotificationSerializer
from messaging.serializers import MessageSerializer


def update_conversation(user_id, serialized_conversation):
    channel_layer = get_channel_layer()
    content =  {
                'type' : 'conversation-update',
                'conversation' : serialized_conversation
            } 
    async_to_sync(channel_layer.group_send)(
        f'general-data-{user_id}',  # Group name to target
        {
            'type': 'send_conversation',  # Method name in consumer to handle the message
            'content': content
           
        }
    )

def update_notification(user_id, notification):
    channel_layer = get_channel_layer()
    serializer_notification = NotificationSerializer(notification).data
    async_to_sync(channel_layer.group_send)(
        f'general-data-{user_id}', 
        {
            'type' : 'send_notification',
            'notification' : notification,
            'serializer_notification' : serializer_notification
        }
    )

def delete_notification(user_id, notification_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'general-data-{user_id}', 
        {
            'type' : 'delete_notification',
            'notification_id' : notification_id,
        }
    )

def update_message(user_id, friend_id, message):
    channel_layer = get_channel_layer()
    serializer_message = MessageSerializer(message).data
    async_to_sync(channel_layer.group_send)(
        f'chatroom-{min(user_id, friend_id)}-{max(user_id, friend_id)}', 
        {
            'type' : 'send_message',
            'message' : message,
            'serializer_message' : serializer_message
        }
    )