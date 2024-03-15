from django.urls import path
from. import views

urlpatterns = [
    path('get-article/', views.get_article),
    path('get-simular-articles/', views.get_simular_articles),
    path('get-article-comments/', views.get_article_comments),
    path('delete-comment/', views.delete_comment),
    path('create-comment/', views.create_comment),
    path('like-article/', views.like_article),
    path('dislike-article/', views.dislike_article),
    path('toggle-save-article/', views.toggle_save_article),
    path('search-articles/', views.serach_articles),
    path('suggest-articles/', views.article_suggestions),
    path('article-other-info/', views.article_other_info),

]
