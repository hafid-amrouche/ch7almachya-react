# Generated by Django 4.2.7 on 2023-12-14 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_brand_article_color_article_document_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='creator',
        ),
    ]