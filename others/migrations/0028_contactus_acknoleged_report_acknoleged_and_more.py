# Generated by Django 4.2.7 on 2024-03-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0027_rename_extra_text_notification_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='acknoleged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='acknoleged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='ruled_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
