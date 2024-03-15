from django.db import models
from user.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    is_seen_by_receiver = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']  # Order messages by timestamp in descending order

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_conversations')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_conversations')
    is_acknowledged = models.BooleanField(default=False)
    last_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        unique_together = ['user1', 'user2']
    
    class Meta:
        ordering = ['-last_message__sent_at']  # Order messages by timestamp in descending order

    