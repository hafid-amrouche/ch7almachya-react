# Generated by Django 4.2.7 on 2024-01-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_image_update_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='credibility',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='scoore',
            field=models.PositiveIntegerField(default=0),
        ),
    ]