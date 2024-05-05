from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('reports/', views.reports),
    path('reports/<int:report_id>/', views.get_report),
    path('messages/', views.messages),
    path('messages/<int:message_id>/', views.get_message),
    path('delete-reported-object/', views.delete_reported_object),
    path('keep-reported-object/', views.keep_reported_object),
    path('reply-to-message/', views.reply_to_message),
    path('send-email/', views.send_email_view),
]
