from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from others.models import Notification, State
from django.utils import timezone

# Create your models here.



class UserExtention(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extention')
    bio = models.TextField(max_length=255, default='')
    email_verified = models.BooleanField(default= False)
    email_public = models.BooleanField(default= True)
    is_page = models.BooleanField(default= False)
    facebook = models.TextField(max_length=255, default='')
    instagram = models.TextField(max_length=255,default='')
    tiktok = models.TextField(max_length=255, default='')
    youtube = models.TextField(max_length=255, default='')
    twitter = models.TextField(max_length=255,default='')
    linkedin = models.TextField(max_length=255, default='')
    other_socials = models.TextField(default='[]')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_male = models.BooleanField(default = True)
    birth_day = models.DateField(null=True, blank=True)
    birth_day_public = models.BooleanField(default= True)
    
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    website = models.TextField(max_length=255, default='')
    is_verified = models.BooleanField(default = False)

class Location(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey('others.state', on_delete=models.CASCADE, default=1)
    city = models.CharField(max_length=50, default='')
    address = models.TextField(max_length=255,  default='')
    location_public = models.BooleanField(default= True)
    


def create_notification_on_follow(follower, leader):
    if follower != leader :
        Notification.objects.create(
            notification_type = 'follow',
            notifier=follower,
            notified=leader,
        )

def delete_notification_on_unfollow(follower, leader):
    try:
        Notification.objects.get(
            notification_type = 'follow',
            notifier=follower,
            notified=leader,
        ).delete()
    except:
        pass

class Followers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers_list = models.ManyToManyField(User, related_name='followers_list')
    def add_follower(self, new_follower):
        if new_follower != self.user:
            self.followers_list.add(new_follower)
            create_notification_on_follow(new_follower, self.user)

    def remove_follower(self, new_follower):
        if new_follower != self.user:
            self.followers_list.remove(new_follower)
            delete_notification_on_unfollow(new_follower, self.user)
            
@receiver(post_save, sender=User)
def user_created_callback(sender, instance, created, **kwargs):
    if created: 
        Followers.objects.create(user=instance)

class UserSuggestion(models.Model):
    text = models.CharField(max_length=100)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_reviews')
    rating = models.SmallIntegerField(null=True, blank=True)

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')
    token = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    def is_expired(self):
        return timezone.now() - self.created_at > timezone.timedelta(seconds=30)

class FCMToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fcm_tokens')
    user_token = models.OneToOneField(UserToken, on_delete=models.CASCADE, related_name='fcm_token')
    token = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)


class DeletedAccount(models.Model):
    username = models.TextField()
    password = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

class UserPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='unhashed_password')
    password = models.TextField()


class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='image') 
    url = models.TextField(default="")
    path = models.TextField(default="")
    url_150 = models.TextField(default="")
    path_150 = models.TextField(default="")

