# Generated by Django 4.2.7 on 2024-02-16 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='credibility',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='scoore',
        ),
    ]