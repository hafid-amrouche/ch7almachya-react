# Generated by Django 4.2.7 on 2024-02-09 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_usersuggestion_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersuggestion',
            name='times',
        ),
    ]
