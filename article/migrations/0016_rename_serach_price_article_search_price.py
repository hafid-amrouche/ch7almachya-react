# Generated by Django 4.2.7 on 2024-02-03 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_article_serach_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='serach_price',
            new_name='search_price',
        ),
    ]
