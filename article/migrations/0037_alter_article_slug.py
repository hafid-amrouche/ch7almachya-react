# Generated by Django 4.2.7 on 2024-03-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0036_article_other_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.TextField(),
        ),
    ]