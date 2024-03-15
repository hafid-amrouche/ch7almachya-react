from django.urls import path
from. import views

urlpatterns = [
    path('create-article/', views.create_article),
    path('update-article/', views.update_article),
    path('get-articles/', views.get_user_articles),
    path('delete-article/', views.delete_article),
    path('delete-image/', views.delete_image),
    path('saved-articles/', views.saved_articles),
    path('get-article-for-edit/', views.get_article_for_edit),
    path('set-main-image/', views.set_main_image),
]
