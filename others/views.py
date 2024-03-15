from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Notification
from .serializers import NotificationSerializer
import time, json

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    time.sleep(1)
    seen_notifications = json.loads(request.POST.get('seen-notifications'))
    try:
        notifications = Notification.objects.filter(notified = request.user).exclude(id__in=seen_notifications)
        cond = notifications.count() > 20
        notifications.update(is_acknowledged=True)
        notifications = notifications[:20]
        notifications = NotificationSerializer(notifications, many=True).data
        return Response([notifications, cond])
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unacknoledged_conversations_count(request):
    time.sleep(1)
    un = Notification.objects.filter(notified = request.user ,is_acknowledged = False).values_list('id', flat=True)
    print(un)
    return JsonResponse(list(un), safe=False, status =200)