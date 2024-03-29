from django.db.models.signals import post_save, pre_delete
from .models import Notification
from user.update_user_realtime_data import update_notification, delete_notification
from user.push_notifications import send
from django.utils.translation import gettext as _


def update_user_notifications(sender, instance, created, **kwargs):
    if created:
        notification = instance
        update_notification(notification.notified.id, notification)

        title = notification.notifier.page.name if notification.notifier.extention.is_page else notification.notifier.get_full_name()

        notification_type = notification.notification_type
        text = notification.text
        link= ''
        if not text:
            if notification_type == 'like':
                text = _('has liked your article "{}"').format(notification.article.title)
                link = f'/@{notification.notified.username}/{notification.article.brand.name.lower()}-{notification.article.title}-{notification.article.id}/'
            elif notification_type == 'dislike':
                text = _('has disliked your article "{}"').format(notification.article.title)
                link = f'/@{notification.notified.username}/{notification.article.brand.name.lower()}-{notification.article.title}-{notification.article.id}/'
            elif notification_type == 'comment':
                text = _('has commented your article "{}"').format(notification.article.title)
                link = f'/@{notification.notified.username}/{notification.article.brand.name.lower()}-{notification.article.title}-{notification.article.id}/'
            elif notification_type == 'follow':
                text = _('has started following you')
                link = f'/@{notification.notifier.username}/'
            elif notification_type == 'leader_posted':
                text = _('has posted an article "{}"').format(notification.article.title)
                link = f'/@{notification.notifier.username}/{notification.article.brand.name.lower()}-{notification.article.title}-{notification.article.id}'
            else:
                text = ''
                
        icon = notification.notifier.extention.image_150
        send(notification.notified, title=title, body=text, link=link, icon=icon, type=f'{notification.notification_type}-{ notification.notifier.id }')

def deleted_user_notification(sender, instance, **kwargs):
    notification = instance
    delete_notification(notification.notified.id, notification.id)

post_save.connect(update_user_notifications, Notification)
# pre_delete.connect(deleted_user_notification, Notification)