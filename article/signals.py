from django.db.models.signals import post_save
from .models import Article, Like, Dislike, Comment
from others.models import Notification



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