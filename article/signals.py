from django.db.models.signals import pre_delete, post_save
from .models import Article, Like, Dislike, Comment, Image
from others.models import Notification
import os
from ch7almachya.settings import BASE_DIR
from functions import delete_folder
from user.models import User

def delele_image_path(sender, instance, *args, **kwargs):
    image = instance
    try :
        os.remove(image.path)
    except Exception as e:
        print(e)

pre_delete.connect(delele_image_path, Image)


def delete_article_folder(sender, instance, *args, **kwargs):
    article = instance
    path = BASE_DIR / f'media/users/{article.creator.id}/articles/{article.id}'
    delete_folder(path)

pre_delete.connect(delete_article_folder, Article)

def create_notification_on_like(sender, instance, created, **kwargs):
    if created and (instance.liker != instance.article.creator):
        Notification.objects.create(
            notification_type = 'like',
            notifier=instance.liker,
            notified=instance.article.creator,
            article=instance.article,
            like = instance
        )

post_save.connect(create_notification_on_like, Like)

def create_notification_on_dislike(sender, instance, created, **kwargs):
    if created and (instance.disliker != instance.article.creator):
        Notification.objects.create(
            notification_type = 'dislike',
            notifier=instance.disliker,
            notified=instance.article.creator,
            article=instance.article,
            dislike = instance
        )
post_save.connect(create_notification_on_dislike, Dislike)

def create_notification_on_comment(sender, instance, created, **kwargs):
    if created and (instance.commenter != instance.article.creator) :
        Notification.objects.create(
            notification_type = 'comment',
            notifier=instance.commenter,
            notified=instance.article.creator,
            article=instance.article,
            comment = instance
        )
post_save.connect(create_notification_on_comment, Comment)


def create_notification_on_leader_post(sender, instance, created, **kwargs):
    if created:
        for follower in instance.creator.followers.followers_list.all():
            Notification.objects.create(
                notification_type = 'leader_posted',
                notifier=instance.creator,
                notified=follower,
                article = instance
            )
post_save.connect(create_notification_on_leader_post, Article)