from django.urls import path
from . import views

urlpatterns = [
    path('get-notifications/', views.get_notifications),
    path('get-unacknoledged-conversations-count/', views.get_unacknoledged_conversations_count)
]
