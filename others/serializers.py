from rest_framework import serializers
from others.models import State, Notification, Ad
from django.utils.translation import gettext as _

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name', 'code']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        name_lang = self.context.get('name_lang') or 'name'
        return getattr(obj, name_lang)
    
class NotificationSerializer(serializers.ModelSerializer):
    notifier_name = serializers.SerializerMethodField(read_only=True)
    def get_notifier_name(self, obj):
        return {'text' :obj.notifier.page.name, 'is_verified': obj.notifier.page.is_verified } if obj.notifier.extention.is_page else obj.notifier.get_full_name()
    
    avatar = serializers.SerializerMethodField(read_only=True)
    def get_avatar(self, obj):
        return obj.notifier.extention.image_150
    
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        if obj.notification_type in ['like', 'dislike', 'comment']:
            return f'/@{obj.notified.username}/{obj.article.brand.name.lower()}-{obj.article.title}-{obj.article.id}/'
        elif obj.notification_type == 'leader_posted':
            return f'/@{obj.notifier.username}/{obj.article.brand.name.lower()}-{obj.article.title}-{obj.article.id}/'
        elif obj.notification_type == 'follow':
            return f'/@{obj.notifier.username}/'
        
    text = serializers.SerializerMethodField(read_only=True)
    def get_text(self, obj):
        text = ''
        notification_type = obj.notification_type
        if notification_type == 'like':
            text = _('has liked your article "{}"').format(obj.article.title)
        
        elif notification_type == 'dislike':
            text = _('has disliked your article "{}"').format(obj.article.title)
        
        elif notification_type == 'comment':
            text = _('has commented your article "{}"').format(obj.article.title)
        
        elif notification_type == 'follow':
            text = _('has started following you')
        
        elif notification_type == 'leader_posted':
            text = _('has posted an article "{}"').format(obj.article.title)


        return text
    
    class Meta:
        model = Notification
        fields = ['notification_type', 'created_at', 'notifier_name', 'text', 'is_seen', 'is_acknowledged', 'id', 'avatar', 'url']

        
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['order', 'url', 'image']