# Generated by Django 4.2.7 on 2024-01-26 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0005_notification_is_acknowledged_notification_is_seen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
