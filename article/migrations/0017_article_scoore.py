# Generated by Django 4.2.7 on 2024-02-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_rename_serach_price_article_search_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='scoore',
            field=models.IntegerField(default=0),
        ),
    ]
