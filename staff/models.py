from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.


class StaffToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_tokens')
    token = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    def is_expired(self):
        return timezone.now() - self.created_at > timezone.timedelta(seconds=30)

class FCMToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_fcm_tokens')
    staff_token = models.OneToOneField(StaffToken, on_delete=models.CASCADE, related_name='fcm_token')
    token = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)