# Generated by Django 4.2.7 on 2024-03-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0025_delete_notificationtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='extra_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
