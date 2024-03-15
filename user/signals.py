from django.db.models.signals import pre_delete


from functions import delete_folder
from ch7almachya.settings import BASE_DIR
from .models import User
from django.contrib.auth.models import User

def delete_user_folder(sender, instance, *args, **kwargs):
    user = instance
    path = BASE_DIR / f'media/users/{user.id}'
    delete_folder(path)



pre_delete.connect(delete_user_folder, User)