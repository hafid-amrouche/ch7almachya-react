# Generated by Django 4.2.7 on 2024-02-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_remove_article_dislikers_remove_article_likers_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='serach_price',
            field=models.IntegerField(default=0),
        ),
    ]
