from django.urls import path
from . import views

urlpatterns = [
    path('send-message/', views.send_message),
    path('get-messages/', views.get_messages),
    path('get-conversations/', views.get_conversations)
]
