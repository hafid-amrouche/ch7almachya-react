# Generated by Django 4.2.7 on 2023-12-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_city_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
