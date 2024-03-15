from django.db import models
from user.models import User
from article.models import Like, Dislike, Comment, Article

class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
        ('leader_posted', 'LeaderPosted'),
    )
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    notifier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifier_notifications', null=True, blank=True)
    notified = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notified_notifications', null=True, blank=True)
    like = models.ForeignKey(Like, on_delete=models.CASCADE, null=True, blank=True)
    dislike = models.ForeignKey(Dislike, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    is_seen = models.BooleanField(default=False)
    is_acknowledged = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at'] 

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now =True)

class Ad(models.Model):
    AD_TYPES = (
        ('swiper', 'Swiper'),
        ('static', 'Static'),
    )
    ad_type= models.CharField(max_length=20, choices=AD_TYPES)
    order = models.IntegerField()
    url = models.TextField()
    image = models.ImageField(upload_to='swpiper_ad_images/')

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)
