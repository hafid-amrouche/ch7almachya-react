from rest_framework import serializers
from others.models import State, Notification, Ad, Report, ContactUs
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
        text = obj.text
        if not text:
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

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['reporters_usernames', 'reported_username', 'type', 'link', 'id', 'obj_id', 'acknoleged', 'ruled_deleted', 'rest_of_reporters_count']

    reporters_usernames = serializers.SerializerMethodField(read_only=True)
    def get_reporters_usernames(self, obj):
        reporters = obj.reporters.all()[:10]
        return list(reporters.values_list('username', flat=True))
    
    rest_of_reporters_count = serializers.SerializerMethodField(read_only=True)
    def get_rest_of_reporters_count(self, obj):
        reporters_count = obj.reporters.count() - 10
        return reporters_count if reporters_count > 0 else 0
    
    reported_username = serializers.SerializerMethodField(read_only=True)
    def get_reported_username(self, obj):
        return obj.reporter.username
    
    reported_username = serializers.SerializerMethodField(read_only=True)
    def get_reported_username(self, obj):
        return obj.user.username
    
    type = serializers.SerializerMethodField(read_only=True)
    def get_type(self, obj):
        if obj.comment:
            return 'Comment'
        elif obj.article:
            return 'Article'
        else:
            return 'User'
        
    link = serializers.SerializerMethodField(read_only=True)
    def get_link(self, obj):
        if obj.comment:
            return obj.comment.slug
        elif obj.article:
            return obj.article.slug
        else:
            return f'/@{obj.user.username}/'
        
    obj_id = serializers.SerializerMethodField(read_only=True)
    def get_obj_id(self, obj):
        if obj.comment:
            return obj.comment.id
        elif obj.article:
            return obj.article.id
        else:
            return obj.user.id
        


class ContacUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'