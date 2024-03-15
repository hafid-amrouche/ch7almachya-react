from django.contrib import admin

from .models import Article, Image, Document, GearBox, Fuel, Option, Comment, Brand, Color, ArticleSuggestion, MainImage, Category, SavedArticle

# Register your models here.

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(MainImage)
admin.site.register(Document)
admin.site.register(Fuel)
admin.site.register(GearBox)
admin.site.register(Option)
admin.site.register(Comment)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(ArticleSuggestion)
admin.site.register(Category)
admin.site.register(SavedArticle)