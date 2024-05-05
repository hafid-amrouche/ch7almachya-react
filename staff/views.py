from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializerWithToken
from .models import StaffToken
from others.models import Report, Notification, ContactUs
from others.serializers import ReportSerializer, ContacUsSerializer
from django.contrib.auth.models import User 
from django.utils.translation import gettext as _
from user.models import DeletedAccount
import time
from functions import send_email
from constants import proxy




# Create your views here.
@api_view(['POST'])
def login(request):
    username= request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if not user.is_staff or not user:
        message = {'detail': 'Wrong credentials'}
        return JsonResponse(message, status=400)
    
    serializer = UserSerializerWithToken(user).data
    StaffToken.objects.create(
        user = user,
        token = serializer['token']
    )
    return Response(serializer)

@api_view(['POST'])
def reports(request):
    user = request.user
    if user.is_staff:
        acknoleged = request.POST.get('acknoleged')
        not_acknoleged = request.POST.get('notAcknoleged')
        seen_reports = request.POST.getlist('seenReports[]')
        reports = Report.objects.exclude(id__in = seen_reports )
        if acknoleged == 'true' and not_acknoleged == 'false':
            reports_count = reports.filter(acknoleged=True).count()
            reports = reports.filter(acknoleged=True)[:20]
        elif acknoleged == 'false' and not_acknoleged == 'true':
            reports_count = reports.filter(acknoleged=False).count()
            reports = reports.filter(acknoleged=False)[:20]
        else:
            reports_count = reports.count()
            reports = reports[:20]
        serializer = ReportSerializer(reports, many=True).data
        return Response([serializer, reports_count > 20])
    else:
        return JsonResponse({'detail' : 'error'}, status=400)

@api_view(['GET'])
def get_report(request, report_id):
    user = request.user
    if user.is_staff:
        report = Report.objects.get(id = report_id)
        serializer = ReportSerializer(report).data
        return Response(serializer)
    else:
        return JsonResponse({'detail' : 'error'}, status=400)

@api_view(['POST'])
def delete_reported_object(request):
    time.sleep(1)
    user = request.user
    notifier = User.objects.get(username='ch7almachya')
    if user.is_staff:
        report = Report.objects.get(id=request.POST.get('report_id'))
        if report.acknoleged == False:
            report.ruled_deleted = True
            report.acknoleged = True
            report.save()
            if report.comment:
                comment = report.comment
                Notification.objects.create(
                    is_seen = True,
                    notification_type = 'your_comment_deleted',
                    notifier = notifier,
                    notified = report.user,
                    text = _('Your comment "{}" was deleted').format(comment.text[:20] + '...')
                )
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        is_seen = True,
                        notification_type = 'your_reported_comment_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the comment of user @{} was accepted and we deleted his comment. Thank you for making Ch7al machya a safer place').format(report.user)
                    )
                comment.delete()
            elif report.article:
                article = report.article
                Notification.objects.create(
                    notification_type = 'your_article_deleted',
                    notifier = notifier,
                    notified = report.user,
                    text = _('Your article "{}" was deleted').format(article.brand.name + ' - ' + article.title),
                    is_seen = True,
                )
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        notification_type = 'your_reported_article_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the article of user @{} was accepted and we deleted his article. Thank you for making Ch7al machya a safer place').format(report.user),
                        is_seen = True,
                    )
                article.delete()
            elif report.user:
                user = report.user
                try:
                    DeletedAccount.objects.create(
                        username = user.username,
                        password = user.unhashed_password.password
                    )
                except:
                    pass
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        notification_type = 'your_reported_user_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the user @{} was accepted and we deleted his account. Thank you for making Ch7al machya a safer place').format(report.user),
                        is_seen = True,
                    )
                if not user.is_staff:
                    user.delete()
            return JsonResponse({
                'acknoleged' : True,
                'ruled_deleted' : True
            })
    else:
        return JsonResponse({'detail' : 'error'}, status=400)

@api_view(['POST'])
def keep_reported_object(request):
    time.sleep(1)
    user = request.user
    notifier = User.objects.get(username='ch7almachya')
    if user.is_staff:
        report = Report.objects.get(id=request.POST.get('report_id'))
        if report.acknoleged == False:
            report.acknoleged = True
            report.save()
            if report.comment:
                comment = report.comment
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        notification_type = 'your_reported_comment_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the comment "{}" was reviewed and we decided not to delete his comment.').format(comment.text[:20] + '...'),
                        is_seen = True,
                    )
            elif report.article:
                article = report.article
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        notification_type = 'your_reported_article_not_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the article "{}" was reviewed and we decided no to delete his article.').format(article.brand.name + ' - ' + article.title),
                        is_seen = True,
                    )
            elif report.user:
                user = report.user
                for reporter in report.reporters.all():
                    Notification.objects.create(
                        notification_type = 'your_reported_user_not_deleted',
                        notifier = notifier,
                        notified = reporter,
                        text = _('Your report on the user @{} was reviewed and we decided not to delete his account.').format(report.user),
                        is_seen = True,
                    )
            return JsonResponse({
                'acknoleged' : True
            })
    else:
        return JsonResponse({'detail' : 'error'}, status=400)
       
@api_view(['POST'])
def reply_to_message(request):
    time.sleep(1)
    user = request.user
    message_id = request.POST.get('message_id')
    message = ContactUs.objects.get(id = message_id)
    reply = request.POST.get('reply').strip()
    logo = f'{ proxy }/static/others/logo.jpg'
    send_email(message.email, reply, logo, 'Ch7al machya')
    message.acknoleged = True
    message.reply = reply
    message.save()
    if user.is_staff:
        return JsonResponse({'reply' : reply})
    else:
        return JsonResponse({'detail' : 'error'}, status=400)
    
@api_view(['POST'])
def messages(request):
    user = request.user
    if user.is_staff:
        acknoleged = request.POST.get('acknoleged')
        not_acknoleged = request.POST.get('notAcknoleged')
        seen_messages = request.POST.getlist('seenMessages[]')
        messages = ContactUs.objects.exclude(id__in = seen_messages )
        if acknoleged == 'true' and not_acknoleged == 'false':
            messages_count = messages.filter(acknoleged=True).count()
            messages = messages.filter(acknoleged=True)[:20]
        elif acknoleged == 'false' and not_acknoleged == 'true':
            messages_count = messages.filter(acknoleged=False).count()
            messages = messages.filter(acknoleged=False)[:20]
        else:
            messages_count = messages.count()
            messages = messages[:20]
        serializer = ContacUsSerializer(messages, many=True).data
        return Response([serializer, messages_count > 20])
    else:
        return JsonResponse({'detail' : 'error'}, status=400)
    
@api_view(['GET'])
def get_message(request, message_id):
    user = request.user
    if user.is_staff:
        messages = ContactUs.objects.get(id = message_id)
        serializer = ContacUsSerializer(messages).data
        return Response(serializer)
    else:
        return JsonResponse({'detail' : 'error'}, status=400)
    
@api_view(['POST'])
def send_email_view(request):
    user = request.user
    if user.is_staff:
        email = request.POST.get('email')
        message = request.POST.get('message')
        title = request.POST.get('title')
        logo = f'{ proxy }/static/others/logo.jpg'
        try:
            send_email(email, title, message, logo)
            return JsonResponse({'datail': 'Email was sent succefully'})
        except:
            return JsonResponse({'datail': 'Email was not sent'}, status=400)
    else:
        return JsonResponse({'datail': 'Email was not sent'}, status=400)
 