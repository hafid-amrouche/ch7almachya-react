from django.urls import path
from . import views

urlpatterns = [
    path('update-profile/', views.update_profile),
    path('update-location/', views.update_location),
    path('update-account/', views.update_account),
    path('update-page/', views.update_page),
    path('update-socials/', views.update_socials),
    path('update-profile-image/', views.update_profile_image),
    path('remove-profile-image/', views.remove_profile_image),
    path('set-email/', views.set_email),
    path('update-email/', views.update_email),
    path('confirm-email/', views.confirm_email),
    path('delete-email/', views.delete_email),
    path('delete-account/', views.delete_account),
    path("confirm-email-activation/<uidb64>/<token>/", views.confirm_email_activation, name='confirm-activation'),
    path('change-password/', views.change_password),
    path('update-username/', views.update_username)
]
