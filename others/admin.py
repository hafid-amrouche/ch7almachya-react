from django.contrib import admin
from .models import State, Notification, Report, Ad, ContactUs
# Register your models here.

admin.site.register(State)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(Ad)
admin.site.register(ContactUs)