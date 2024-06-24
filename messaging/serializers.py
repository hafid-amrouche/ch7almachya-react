from rest_framework import serializers
from rest_framework.fields import empty
from .models import Message, Conversation
from functions import get_media_url

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'is_seen_by_receiver', 'text', 'sent_at', 'id']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'friend_id', 'friend_name', 'text', 'friend_image', 'sent_at', 'is_seen', 'message_sender']

    friend_name = serializers.SerializerMethodField()
    def get_friend_name(self, obj):
        user = self.context['user']
        friend = obj.user2 if user == obj.user1 else obj.user1
        return {'text' :friend.page.name, 'is_verified': friend.page.is_verified } if friend.extention.is_page else friend.get_full_name()
    
    message_sender = serializers.SerializerMethodField()
    def get_message_sender(self, obj):
        return obj.last_message.sender.id
    
    friend_id = serializers.SerializerMethodField()
    def get_friend_id(self, obj):
        user = self.context['user']
        friend = obj.user2 if user == obj.user1 else obj.user1
        return friend.id
    
    text = serializers.SerializerMethodField()
    def get_text(self, obj):
        return obj.last_message.text
    
    def get_friend_image(self, obj):
        user = self.context['user']
        friend = obj.user2 if user == obj.user1 else obj.user1
        try :
            return get_media_url(friend.image.url_150)
        except:
            if friend.extention.is_page:
                return '/static/others/page_icon_150.png'
            else:
                return '/static/others/user_150.png'
    
    friend_image = serializers.SerializerMethodField(read_only=True)
    def get_friend_image(self, obj):
        user = self.context['user']
        friend = obj.user2 if user == obj.user1 else obj.user1
        try :
            return get_media_url(friend.image.url_150)
        except:
            if friend.extention.is_page:
                return '/static/others/page_icon_150.png'
            else:
                return '/static/others/user_150.png'

    sent_at = serializers.SerializerMethodField()
    def get_sent_at(self, obj):
        return obj.last_message.sent_at
    
    is_seen = serializers.SerializerMethodField()
    def get_is_seen(self, obj):
        return obj.last_message.is_seen_by_receiver
