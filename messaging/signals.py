from django.db.models.signals import post_save
from .models import Message
from user.update_user_realtime_data import update_message
from user.push_notifications import send

def update_user_messages(sender, instance, created, **kwargs):
    if created:
        message = instance
        update_message(message.receiver.id, message.sender.id, message)

        title = message.sender.page.name if message.sender.extention.is_page else message.sender.get_full_name()
        link = f'/messages/{message.sender.id}/'
        try:
            icon= message.sender.image.url_150
        except:
            if message.sender.extention.is_page:
                icon = '/static/others/page_icon_150.png'
            else:
                icon = '/static/others/user_150.png'
        send(message.receiver, title=title, body=message.text, link=link, icon=icon , type=f'message-{message.sender.id}')


post_save.connect(update_user_messages, Message)
