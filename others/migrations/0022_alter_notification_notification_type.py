# Generated by Django 4.2.7 on 2024-03-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0021_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(max_length=20),
        ),
    ]
