# Generated by Django 4.2.7 on 2024-03-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0059_fcmtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcmtoken',
            name='last_active',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
