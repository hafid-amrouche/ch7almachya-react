from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('refresh-user-token/', views.refresh_user_token),
    path('update-fcm-token/', views.update_fcm_token),
    path('logout/', views.logout),
    path('register/', views.registerUser),
    path('profile/<username>/', views.get_profile),
    path('profile/<username>/get-articles/', views.get_user_articles),
    path('profile/<username>/toggle-follower/', views.toggle_follower),
    path('search-users/', views.serach_users),
    path('search-pages/', views.search_pages),
    # path('suggest-users/', views.users_suggestions),
    # path('suggest-pages/', views.pages_suggestions),
    path('get-user-about/', views.get_user_about),
    path('add-review/', views.rate_user)
]
