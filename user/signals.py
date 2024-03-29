from django.db.models.signals import pre_delete


from functions import delete_folder
from ch7almachya.settings import BASE_DIR
from .models import User, UserSuggestion
from django.contrib.auth.models import User

def pre_delete_user(sender, instance, *args, **kwargs):
    user = instance
    path = BASE_DIR / f'media/users/{user.id}'
    try:
        delete_folder(path)
    except:
        pass
pre_delete.connect(pre_delete_user, User)