# Generated by Django 4.2.7 on 2024-05-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0076_alter_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextention',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userextention',
            name='image_150',
        ),
    ]
