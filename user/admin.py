from django.contrib import admin
from .models import Profile, Followers, UserSuggestion, Review, UserExtention, Page, Location, UserToken, FCMToken, UserPassword
# Register your models here.


admin.site.register(Profile)
admin.site.register(Followers)
admin.site.register(UserSuggestion)
admin.site.register(Review)
admin.site.register(UserExtention)
admin.site.register(Page)
admin.site.register(Location)
admin.site.register(FCMToken)
admin.site.register(UserToken)
admin.site.register(UserPassword)


