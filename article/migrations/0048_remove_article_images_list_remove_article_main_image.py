# Generated by Django 4.2.7 on 2024-04-15 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0047_alter_article_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='images_list',
        ),
        migrations.RemoveField(
            model_name='article',
            name='main_image',
        ),
    ]
